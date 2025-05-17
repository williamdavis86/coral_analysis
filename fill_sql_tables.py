import sqlite3
import pandas as pd

# load the csv dataset created by ingest_data.py
df = pd.read_csv('coral_raw.csv')

# Connect to the SQLite database
conn = sqlite3.connect('coral.sqlite')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# load the schema defined in schema.sql
with open('schema.sql', 'r') as f:
    cursor.executescript(f.read())

# commit the changes
conn.commit()

# Insert data into the tables

# dicts to map scientific names to ids
species_dict = {}
locations_set = {}

# function to safely handle NaN values
def safe(val):
    return None if pd.isna(val) else val

# Insert data into the species table
for _, row in df.iterrows():
    scientific_name = row.get('scientificName')
    taxon_rank = row.get('taxonRank')
    values = (
        scientific_name,
        taxon_rank,
        row.get('kingdom'),
        row.get('phylum'),
        row.get('class'),
        row.get('order'),
        row.get('family'),
        row.get('genus')
    )
    # Check if the scientific name already exists in the species table
    # if it doesnt exist, insert it
    if scientific_name not in species_dict:
        cursor.execute("""
        INSERT INTO species (scientific_name, taxon_rank, kingdom, phylum, class, "order", family, genus)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", values)
        conn.commit()
        cursor.execute("SELECT species_id FROM species WHERE scientific_name = ?", (scientific_name,))
        species_dict[scientific_name] = cursor.fetchone()[0]

    # Insert data into the locations table
    # use safe() to convert nan to None, which will correctly insert into sql as null

    location_unique = (safe(row.get("decimalLatitude")), safe(row.get("decimalLongitude")), safe(row.get("depth")),
               safe(row.get("country")), safe(row.get("locality")))
    # Check if the location already exists in the locations table
    # if it doesnt exist, insert it
    if location_unique not in locations_set:
        cursor.execute("INSERT INTO locations (decimal_latitude, decimal_longitude, depth, country, locality) VALUES (?, ?, ?, ?, ?)", location_unique)
        conn.commit()
        cursor.execute("""
            SELECT location_id FROM locations
            WHERE decimal_latitude IS ? AND decimal_longitude IS ? AND depth IS ? AND country IS ? AND locality IS ?
        """, location_unique)
        result = cursor.fetchone()

        if result:
            locations_set[location_unique] = result[0]
        else:
            raise ValueError(f"Could not retrieve location after insert: {location_unique}")

    # Insert data into the occurrences table
    cursor.execute("""
        INSERT OR IGNORE INTO occurrences (
            occurrence_id, event_date, species_id, location_id,
            dataset_id, individual_count, basis_of_record
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        row.get('id'),
        row.get('eventDate'),
        species_dict[scientific_name],
        locations_set[location_unique],
        row.get('datasetID'),
        row.get('individualCount'),
        row.get('basisOfRecord')
    ))
conn.commit()
# Close the connection
conn.close()
print("Data inserted successfully into the database.")