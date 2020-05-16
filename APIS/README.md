# WORKING WITH APIS

We wrote a self-contained program to generate a visualization based on data retrieved by the program. The program uses a web API (Application Programming Interface) to request specific information from a website automatically, instead of asking for whole pages. Then this information will be used to generate a visualization. Since programs written in this way will always use current data to generate a visualization, even if that data changes quickly, they will be.

## Using a web API

A web API is a part of a website designed to interact with programs that use very specific URLs in order to request certain information. This type of request is known as an API call. The requested data will be returned in an easily processed format, for example, JSON or CSV. Most applications that rely on external data sources, such as those that integrate with social media sites, rely on API calls.

## Git and GitHub

Our visualization will be based on information from GitHub: a website that allows programmers to collaborate on projects. We will use the GitHub API to request information from the site about Python projects and then we will generate an interactive view of the relative popularity of these projects in Pygal.
With that we can do:

* Processing an API response;
* Working with the response dictionary;
* Summary of the main repositories;
* Monitoring API usage rate limits;
* Viewing repositories using Pygal;
* Perfecting Pygal's graphics;
* Adding custom context hints;
* Plotting the data;
* Adding clickable links to our chart;

## The Hacker News API

To explore the use of API calls on other sites, we'll take a look at Hacker News [Hacker News](http://news.ycombinator.com/). At Hacker News, people share articles about programming and technology, and engage in enthusiastic discussions about those articles. The Hacker News API provides access to data on all submitted articles and website comments, available without the need to register to obtain a key. And with that we followed the same steps that were done on GitHub.
