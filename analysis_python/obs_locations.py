import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("./coral.sqlite")

df = pd.read_sql("""
    select l.decimal_latitude as lat, l.decimal_longitude as lon
    from occurrences o
    inner join locations l on o.location_id = l.location_id
    where l.decimal_latitude is not null and l.decimal_longitude is not null
""", conn)

plt.hexbin(df["lon"], df["lat"], gridsize=100, cmap="viridis", bins='log')
plt.colorbar(label='Observation Count')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Coral Observation Density Map')
plt.tight_layout()
plt.savefig("analysis_python/obs_locations.png")
