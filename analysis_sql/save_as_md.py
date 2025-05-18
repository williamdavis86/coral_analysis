import sqlite3
import pandas as pd

# Run most common coral query
conn = sqlite3.connect("./coral.sqlite")
query = open("analysis_sql/most_common_coral.sql").read()
df = pd.read_sql(query, conn)

# save as markdown
with open("analysis_sql/most_common_coral_results.md", "w") as f:
    f.write(df.to_markdown(index=False, tablefmt="github"))

# Run common coral locations query
query = open("analysis_sql/common_coral_locations.sql").read()
df = pd.read_sql(query, conn)

# save as markdown
with open("analysis_sql/common_coral_locations.md", "w") as f:
    f.write(df.to_markdown(index=False, tablefmt="github"))

# Run snorkel corals query
query = open("analysis_sql/snorkel_corals.sql").read()
df = pd.read_sql(query, conn)

# save as markdown
with open("analysis_sql/snorkel_corals.md", "w") as f:
    f.write(df.to_markdown(index=False, tablefmt="github"))

conn.close()
