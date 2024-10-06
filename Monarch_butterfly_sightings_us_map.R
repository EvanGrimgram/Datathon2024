# author: Aishwarya Patel
# date: 10/06/2024
# project: monarch butterfly sightings by state U.S Map visual

# Install necessary packages for visualization
# install.packages(c("ggplot2", "dplyr", "usmap", "RColorBrewer"))

# Load the libraries
library(ggplot2)
library(dplyr)
library(usmap)
library(RColorBrewer)

# Load the data
data <- read.csv("C:/Users/patela21/Desktop/Datathon 2024/monarch_sightings.csv")

# Summarize the data by state
state_data <- data %>%
  filter(State.Province %in% state.abb) %>%  # Ensure only U.S. states are included
  group_by(State.Province) %>%
  summarize(Sightings = sum(Number)) %>% 
  rename(state = State.Province)

# Merge with map data
us_map_data <- usmap::us_map()
#map_data <- merge(us_map_data, state_data, by.x = "abbr", by.y = "State.Province", all.x = TRUE)

# Fill NA values with 0 for states with no sightings
map_data$Sightings[is.na(map_data$Sightings)] <- 0

# Define a color palette with earth tones
earth_tones <- brewer.pal(9, "YlGn")

# Create the map using the usmap::plot_usmap directly with fill set by state sightings
plot_usmap(data = state_data, values = "Sightings", color = "white") +
  scale_fill_gradientn(colors = earth_tones, na.value = "gray90", name = "Sightings") +
  labs(title = "Monarch Butterfly Sightings by State", fill = "Number of Sightings") +
  theme_minimal() +
  theme(legend.position = "right")

