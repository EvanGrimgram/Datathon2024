import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch the page content
url = "https://journeynorth.org/sightings/querylist.html?map=monarch-adult-spring&year=2024&season=spring"  # the actual URL for monarch sightings
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Locate the table and extract data
table = soup.find('table', class_='querylist')  # Adjust the class name if necessary
sightings_data = []

# Iterate over table rows and extract data
for row in table.find_all('tr')[1:]:  # Skip the header row
    cols = row.find_all('td')
    if len(cols) > 0:
        date = cols[1].text.strip()
        town = cols[2].text.strip()
        state_province = cols[3].text.strip()
        latitude = cols[4].text.strip()
        longitude = cols[5].text.strip()
        number = cols[6].text.strip()
        sightings_data.append([date, town, state_province, latitude, longitude, number])

# Step 4: Convert the data into a Pandas DataFrame
df = pd.DataFrame(sightings_data, columns=['Date', 'Town', 'State/Province', 'Latitude', 'Longitude', 'Number'])

# Step 5: Save or display the DataFrame
if not df.empty:
    df['Number'] = df['Number'].astype(int)  # Convert Number to integer for plotting
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
    plt.xlabel('State/Province')
    plt.ylabel('Number of Sightings')
    plt.show()
else:
    print("No data to plot.")
