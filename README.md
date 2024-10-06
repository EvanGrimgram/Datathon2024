# Pesticide Mapping and the Waning Population of Butterflies - Datathon 2024
The fundamentals of civilization rest on the foundation of food security. When food security becomes compromised, empires collapse and societies fall. Food production is delicate when dealing with environmental factors: temperature, precipitation, humidity, soil properties, climate, and pollinators. These ecological factors profoundly impact the growth and prosperity of our food crops. Many of these variables have recently fluctuated, and some have become more scarce. Pollinators have seen one of the largest declines of all, and have caused times of trouble to our stability. Pesticides are a massive factor in this loss of bio-diversity, our group has been tasked with tracking various pesticides within our states along with Monarch Butterfly immigration to see if we can find a pattern among pollinators and pesticides. Beginner Track.

## Overview of the Pesticide Mapper
Because of the nature of our goal, our project requires us to view a large amount of data regarding pesticide use within the United States and map it by each State. With this goal in mind, we have created a Python application that allows anyone to view the concentration of any given pesticide by State within the United States. Only a small amount of coding is required for this.

### Prerequisites
Before running the code, ensure you have the following installed:
- Python 3.x
- Pandas library
- Plotly library

You can install the required libraries using pip in the Command Prompt: ```pip install pandas plotly```

### Files
The ZIP file 'PesticideMapping.zip' contains the following files needed:
- USDA_PDP_AnalyticalResults_edit.csv: The CSV file with pesticide data.
- PesticideMapping.py: The Python script to generate the map.

### Instructions 
1. **Extract the ZIP file:** Extract the contents of the ZIP file to a directory on your computer.
2. **Navigate to the directory:** Open a terminal or command prompt and navigate to the directory where you extracted the files.
3. **Run the Python script:** Execute the following command to run the Python script: ```python PesticideMapping.py```
4. **Input the pesticide name:** When prompted, enter the name of the pesticide you want to visualize. The input is case-sensitive. Some notable pesticide names you can use are Atrazine, Chlorpyrifos, Imidacloprid, Thiamethoxam, Malathion, and Diazinon.
5. **View the map:** After entering the pesticide name, a map will be generated and displayed, showing the concentration of the selected pesticide by state.

## Mapping Monarch Butterflies
???????????????? Input information here?????????????????????????????????????????

## Limitations and Biases
While our data is very informative and necessary for our project, it is not without its limitations:
- The USDA Pesticide data has some lacking information, especially relating to lesser-known and/or recently banned chemicals. Some states have no information at all regarding some of their pesticides.
- Most of Journey North's data is obtained through voluntary surveys which can have errors and biases. And volunteer contributions do not paint the entire full picture of the population(s).


## Contributers
Our group had the following Hackers involved in this project along with their contributions:
- **John Griffith** - Main developer for the Pesticide Mapper, and managing the projects framework
- **Bella Griffith** - input contributions here
- **name here** - input contributions here
- **name here** - input contributions here
