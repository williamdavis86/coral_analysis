import requests
import pandas as pd

def fetch_coral_data(limit=10000, save_csv=True):
    url = "https://api.obis.org/v3/occurrence"
    params = {
        "scientificname": "Scleractinia", # most modern coral reefs are scleractinian
        "size": limit # limit the number of records returned (csv is approx 10MB with this set to 10000)
    }

    print("getting coral data from OBIS API")
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    records = data.get("results", [])

    if not records:
        print("No results returned from OBIS API")
        return None

    # Normalize the JSON data into a pandas DataFrame
    df = pd.json_normalize(records)

    # save to csv
    if save_csv:
        df.to_csv("coral_raw.csv", index=False)
        print(f"Saved {len(df)} records to coral_raw.csv")

    return df

if __name__ == "__main__":
    fetch_coral_data()
