# OBIS Coral Analysis
## The Data
For my upcoming honeymoon, I have been researching snorkeling, ocean wildlife, and corals. So, for this project, I decided to use
coral data from the [Ocean Biodiversity Information System (OBIS)](https://obis.org/data/access/). The data is accessible via API. I chose to analyze "Scleractinia",
which is the type of coral that makes up most modern reef systems.

## The Pipeline 

To ingest the data, I used the `requests` library to make a request to the OBIS API. 
The data is returned in JSON format, which I then converted into a pandas DataFrame. This is done in `ingest_data.py`.

Then, I put the data into a sqlite database using the `sqlite3` library in `fill_sql_tables.py`. The SQL schema code can be found in `schema.sql`.

For the analysis, I answered three questions with SQL only and two question in Python/SQL. The questions I answered with SQL are 
"Where are corals most often seen?", "What are the most commonly observed corals?", and "What corals are commonly at a depth suitable for snorkeling?".
The result to answer these questions can be seen in their respective md files 
`analysis_sql/comon_coral_locations.md`, `analysis_sql/most_common_coral_results.md`, and `analysis_sql/snorkel_corals.md`.

For the Python analysis, I wanted to inspect the data by checking on observations over time as 
well as a longitude/latitude heat map of where observations have been made. I used `matplotlib` to create the visualizations for these analyses. 
The resulting figures can be seen in `analysis_python/obs_over_time.png` and `analysis_python/obs_locations.png`. 

## Running the Code

The code was written in Python 3.12. To run the code, make sure you have the required packages from `requirements.txt` installed. 
I recommend using a miniconda environment to manage the packages.

Once you have the required packages, you can run `python run_all.py` to ingest the data, fill the tables, and run the analyses.
The results of the analyses are in the md and png files mentioned above.