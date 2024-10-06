# Install necessary libraries:
# pip install requests beautifulsoup4 pandas matplotlib

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch the page content
url = "https://journeynorth.org/sightings/querylist.html?map=monarch-adult-spring&year=2024&season=spring"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Locate the sightings data based on the actual HTML structure
sightings_data = []
table = soup.find('table', class_='views-table')  # Assuming the data is in a table
if table:
    rows = table.find_all('tr')
    for row in rows[1:]:  # Skipping the header row
        cols = row.find_all('td')
        if len(cols) >= 5:  # Adjust this based on number of columns
            date = cols[0].text.strip()
            state = cols[1].text.strip()
            location = cols[2].text.strip()
            number = cols[4].text.strip()
            sightings_data.append([date, state, location, number])

# Step 4: Convert the data into a Pandas DataFrame
df = pd.DataFrame(sightings_data, columns=['Date', 'State/Province', 'Location', 'Number'])

# Step 5: Clean and save the DataFrame
if not df.empty:
    df['Number'] = pd.to_numeric(df['Number'], errors='coerce')  # Convert to numeric, handling errors
    df.dropna(subset=['Number'], inplace=True)  # Drop rows where 'Number' couldn't be converted
    df['Number'] = df['Number'].astype(int)  # Convert to integer after cleaning
    
    # Save to CSV
    df.to_csv('monarch_sightings.csv', index=False)
    print(df)
else:
    print("No data found. Please check the HTML structure and selectors.")

# To visualize:
if not df.empty:
    # Group data by state and sum up the sightings count
    state_sightings = df.groupby('State/Province')['Number'].sum()

    # Plot the data (simple bar chart for example)
    state_sightings.plot(kind='bar', figsize=(10,6))
    plt.title('Monarch Butterfly Sightings by State')
    plt.ylabel('Number of Sightings')
    plt.show()
else:
    print("No data to plot.")
