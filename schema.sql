drop table if exists species;
CREATE TABLE species (
    species_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scientific_name TEXT UNIQUE,
    taxon_rank TEXT,
    kingdom TEXT,
    phylum TEXT,
    class TEXT,
    "order" TEXT,
    family TEXT,
    genus TEXT
);

drop table if exits locations;
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    decimal_latitude REAL,
    decimal_longitude REAL,
    depth REAL,
    country TEXT,
    locality TEXT,
    UNIQUE (decimal_latitude, decimal_longitude, depth, country, locality)
);

drop table if exists occurrences;
CREATE TABLE occurrences (
    occurrence_id TEXT PRIMARY KEY,
    event_date TEXT,
    species_id INTEGER,
    location_id INTEGER,
    dataset_id TEXT,
    individual_count INTEGER,
    basis_of_record TEXT,
    FOREIGN KEY (species_id) REFERENCES species(species_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);
