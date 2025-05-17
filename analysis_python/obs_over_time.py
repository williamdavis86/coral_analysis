import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect to sqlite
conn = sqlite3.connect("../coral.sqlite")

# grab event_date from occurrences table
df = pd.read_sql("""
    SELECT event_date FROM occurrences
    WHERE event_date IS NOT NULL
""", conn)

# convert event_date to datetime
df['event_date'] = pd.to_datetime(df['event_date'], errors='coerce')
df['year'] = df['event_date'].dt.year

# Count observations per year
year_counts = df['year'].value_counts().sort_index()

# plot time series
plt.figure(figsize=(10, 5))
year_counts.plot(kind='line', marker='o', title='Coral Observations Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Observations')
plt.grid(True)
plt.tight_layout()
plt.show()

conn.close()
