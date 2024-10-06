# author: Aishwarya Patel
# date: 10/06/2024
# project: monarch butterfly sightings by state barplot

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
  filter(State.Province %in% state.abb) %>%
  group_by(State.Province) %>%
  summarize(Sightings = sum(Number)) %>%
  rename(state = State.Province)

# Create a custom color palette with earthy tones
colors_tones <- colorRampPalette(c("#26c6da", "#66bb6a", "#ff9800", "#673ab7", "#ffeb3b", "#9ccc65"))(n = nrow(state_data))

# Create the bar plot
ggplot(state_data, aes(x = reorder(state, -Sightings), y = Sightings, fill = state)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = colors_tones) +
  labs(title = "Monarch Butterfly Sightings by State",
       x = "State",
       y = "Number of Sightings") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1),
        legend.position = "none")
