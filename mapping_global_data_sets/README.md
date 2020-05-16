# Mapping global data sets: JSON format

Data from different countries was downloaded in JSON format and we worked with that data using the json module. Using Pygal's beginner-friendly mapping tool for country-based data, we create visualizations of that data to explore global patterns that concern the distribution of the world's population across different countries.
This was done:

* Extraction of relevant data;
 The file basically consists of a long Python list. Each item is a dictionary with four keys: the name of a country, its code, a year and a value that represents the population. We only analyzed the name of each country and the population in 2010;
* Convert strings to numeric values;
 All keys and values in population_data.json are stored as strings. To work with population data, we must convert strings with populations to numeric values. We do this using the int function;
* Obtaining two-letter country codes;
>>> Country codes in Pygal are stored in a module called i18n, which is an abbreviation for internationalization. The COUNTRIES dictionary contains two-letter country codes as keys and country names as values. To view these codes, import the i18n module dictionary and display its keys and values;
* Building a world map;
 With the country codes we have, creating a world map is quick and easy. Pygal includes a type of map called Worldmap to help map global data sets;
* Plotando dados numéricos em um mapa-múndi;
 We put the numerical data of the world population on a map, and with that we create a map that shows the populations of the countries;
* Grouping countries according to their population;
 As China and India are much more populous than other countries, the map shows little contrast. China and India each have more than one billion people, while the next most populous country is the United States, with approximately 300 million people. Rather than plotting all countries as a group, we are going to separate them into three population levels: less than 10 million, between 10 million and 1 billion and above 1 billion;
* Styling world maps with Pygal;
* Lightening the theme color;
