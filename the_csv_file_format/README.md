# DOWNLOADING DATA

Downloading datasets from online sources and creating functional visualizations of that data.
We access and view data stored in two common formats: CSV and JSON. We use the Python csv module to process meteorological data stored in CSV format (Comma-Separated Values, or Comma Separated Values) and analyze the maximum and minimum temperatures over time in two different locations. Then we will use matplotlib to generate a graph based on the downloaded data and display the temperature variations in two very different environments: Sitka in Alaska and Death Valley in California.

A simple way to store data in a text file is to write it as a series of comma-separated values. The resulting files are called CSV files.
They are weather data for January 5, 2014 for Sitka in Alaska. They include the maximum and minimum temperatures as well as several other measurements from that day. CSV files can be complicated for humans to read, but they are easy for programs to process and extract values, which streamlines the data analysis operation.

# Parsing CSV file headers

The csv module of the standard Python library parses the lines of a CSV file and allows you to quickly extract the values we are interested in. We start by analyzing the first line of the file, which contains a series of headers for the data.
Then it was done:

* Displaying headers and their positions;
* Extracting and reading data;
* Plotting data on a temperature graph;
* Datetime module;
>>> We've added dates to our chart to make it more useful;
* Plotting Dates;
>>> Extracting the daily maximum dates and passing the maximum dates and temperatures to plot;
* Plotting a longer period of time;
* Plotting a second data series;
>>> Including minimum temperatures;

### Shading an area of the chart

After adding two series of data, we can now analyze the temperature variation for each day. We will add a final touch to the graph using shading to show the variation between minimum and maximum temperatures each day. For this we will use the fill_between method, which accepts a series of x values and two series of y values, and fills the space between the two series of y values.

### Error checking

some weather stations occasionally malfunction and fail to collect some of the data they are supposed to obtain - or all of them. The absence of data can result in exceptions that can cause our programs to fail if we do not handle them properly.
