import subprocess

# run ingest_data to create the csv file
subprocess.run(["python", "ingest_data.py"], check=True)

# run fill_sql_tables to create the sqlite database
subprocess.run(["python", "fill_sql_tables.py"], check=True)

# run save_as_md to create the markdown files
subprocess.run(["python", "analysis_sql/save_as_md.py"], check=True)

# run obs_location to create the obs_location.png file
subprocess.run(["python", "analysis_python/obs_locations.py"], check=True)

# run obs_over_time to create the obs_over_time.png file
subprocess.run(["python", "analysis_python/obs_over_time.py"], check=True)
#