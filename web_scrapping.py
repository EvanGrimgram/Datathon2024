# Install necessary libraries:
# pip install requests beautifulsoup4 pandas matplotlib

# Web Scraping Code:
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch the page content
url = "https://journeynorth.org/sightings/querylist.html?map=monarch-adult-spring&year=2024&season=spring"  # Replace this with the actual URL for monarch sightings
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Locate the sightings data (this part depends on the actual HTML structure of the website)
sightings_data = []
for entry in soup.find_all('div', class_='sighting-entry'):  # Adjust the class name accordingly
    state = entry.find('span', class_='State/Province')
    count = entry.find('span', class_='Number')
    if state and count:  # Check if the elements are found
        sightings_data.append([state.text, count.text])

# Step 4: Convert the data into a Pandas DataFrame
df = pd.DataFrame(sightings_data, columns=['State', 'Count'])

# Step 5: Save or display the DataFrame
if not df.empty:
    df['Count'] = df['Count'].astype(int)  # Convert Count to integer for plotting
    df.to_csv('monarch_sightings.csv', index=False)
    print(df)
else:
    print("No data found. Please check the HTML structure and selectors.")

# To visualize:
if not df.empty:
    # Group data by state and sum up the sightings count
    state_sightings = df.groupby('State')['Count'].sum()

    # Plot the data (simple bar chart for example)
    state_sightings.plot(kind='bar', figsize=(10,6))
    plt.title('Monarch Butterfly Sightings by State')
    plt.ylabel('Number of Sightings')
    plt.show()
else:
    print("No data to plot.")
