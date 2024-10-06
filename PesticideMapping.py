import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
df = pd.read_csv('USDA_PDP_AnalyticalResults_edit.csv', low_memory=False)

# Prompt the user to input the pesticide name
pesticide = input("Enter the pesticide name: ")

# PESTICIDE NAMES: Atrazine, Chlorpyrifos, Glyphosate, Imidacloprid, '2,4-D'

# Filter the dataframe for the selected pesticide
data = df[df['Pesticide Name'] == pesticide][['State', 'Concentration']].copy()

# Ensure concentration values are numeric
data['Concentration'] = pd.to_numeric(data['Concentration'], errors='coerce')

# Drop rows with missing concentration values
data = data.dropna(subset=['Concentration'])

# Group by state and keep the top value per state
data = data.groupby('State', as_index=False).max()

# Create the color-coded map
fig = go.Figure(data=go.Choropleth(
    locations = data['State'],
    z = data['Concentration'],
    locationmode = 'USA-states',
    colorscale = 'Viridis',
    marker_line_color = 'white',  # Line markers between states
    colorbar_title = pesticide + ' Concentration'
))

# Add annotations for each state
for i, row in data.iterrows():
    fig.add_annotation(
        x = row['State'],
        y = row['Concentration'],
        text = str(row['Concentration']),
        showarrow = False,
        font = dict(color='black', size=12)
    )

# Update layout for better visualization
fig.update_layout(
    title_text = pesticide + ' Concentration by State',
    geo = dict(
        lakecolor = 'rgb(255, 255, 255)',
        projection_type = 'albers usa'
    )
)

# Show the map
fig.show()
