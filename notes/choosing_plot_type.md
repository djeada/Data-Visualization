## Intro
Data visualization is used at several phases of the data science process:

* At the very beginning, to gain early insights into an unknown data set.
* Finally, when the data has been collected, analyzed, and modeled, the relationships must be shown in order to draw conclusions.

We employ data visualization as a tool for communicating data insights through visual representation.
Graphs, charts, maps, and diagrams aid in the understanding of complicated data, the discovery of patterns, the identification of trends and making of predictions.

There is no silver bullet. Each plot type has its advantages and disadvantages. Before deciding on a plot type, consider the following questions:

* What do you wish to emphasize or demonstrate?
  - How much / what percent?
  - Trends
  - Correlation
  - Geographic insights  
* Which visualization makes the data as easy to read and analyze as possible?
* What is the standard technique of displaying data in your field (to avoid confusion)?
* Does it still make sense in black and white (some people may want to print out your plots)? 

Let's look at different graphs and charts grouped by their purpose:

## Show relationship 

A relationship approach is used to show a connection or correlation between two or more variables.

### 1. Bar Chart
Bar charts are useful for displaying the amount of different types of items at a certain point in time. The one axis of the chart represents the specific categories being compared, while the other axis represents a measured value.

![Capture](https://user-images.githubusercontent.com/37275728/184005258-9f3884b8-3ed5-49d1-8b44-2b760e6fc1b6.PNG)

Be aware that vertical bar charts and histograms are not the same thing (even though they look similarly). Histograms depict continuous changes over time.

Vertical bar charts are frequently used to compare a single category of data to individual sub-items. 

#### Usecases
* Revenue across areas.

### 2. Scatter plot
A scatter plot is a common type of graph in science. It is composed of several data points plotted on two axes.

![Capture](https://user-images.githubusercontent.com/37275728/184005392-a9576de8-6175-4c88-a297-d7b6e1e86f2d.PNG)

A scatter plot is used to determine the data's relationship with each variable, such as correlation or trend patterns. It also aids in the detection of outliers in the dataset.

#### Usecases
* Display the relationship between GPA and first salary.

#### Disadvantages
* If we want to investigate time patterns, scatter plots are unproductive.
* A scatter plot is also not the best choice for categorical data.

### 3. Bubble Chart
When we want to illustrate three variables simultaneously, we commonly utilize bubble charts (as opposed to showing only 2 in scatter plot).
One variable is shown on the x-axis, another on the y-axis, and the third as the size of the bubble.

#### Usecases
* The relationship between life expectancy, per capita GDP and population size. 

## Plotting data over time
Sometimes knowing that a relationship exists between variables isn't enough; in certain circumstances, deeper analysis is suitable if we can additionally visualize when the relationship actually happened.
The time appears as a link attribute because relationships are expressed by connections between variables.
This visualization style displays data across time to identify the  patterns. 

### 1. Line Chart
Line charts are used to depict quantitative values across time.

Line charts are created by first connecting data points on a cartesian coordinate grid.
The y-axis usually has a numerical value, whereas the x-axis represents a timeframe or a series of intervals.

The graph's line orientation serves as a great metaphor for the data: an upward slope suggests growing values, while a downward slope shows decreasing values. All of the lines have the potential to indicate patterns in variable changes. 

#### Usecases
* Revenue in dollars over time
* Energy consumption in kWh over time
* Google searches over time

### 2. Area Chart

An area chart is built on the concept of a line chart. The colored area depicts the distribution of the total value over time. Area charts are excellent for displaying the amount of change between two or more data points.

#### Usecases
* Total sales over time
* Active users over time

#### Disadvantages
* Area charts are not the best choice if we want to present fluctuating values, like the stock market or price changes.
* The exact values of the two (or more) areas at a given time cannot be compared directly (line chart is better in that case).

### 3. Stack Area Chart
The stack area chart concept is based on area charts. It shows the value of many groups on the same graph. Each group's values are shown on top of one another.

![Capture](https://user-images.githubusercontent.com/37275728/184005506-e11296cb-a330-4def-b193-cdb4e57b1c6d.PNG)

Stacked area charts are visually appealing and entertaining, but they should be used with caution since they may easily become unreadable. We should not group more than three categories together. 

#### Usecases
* Active users over time by segment
* Total revenue over time by country

#### Disadvantages
* Because stacked area charts only display whole integers, they cannot display negative values.

## Distribution plot
Distribution plots display the distribution of sample data by comparing the empirical distribution of the data to the theoretical values anticipated given a specific distribution.
To assess if the sample data could be described by certain distribution, you can use distribution charts in addition to more formal hypothesis testing. 

### 1. Histogram

Displays a variable's distribution. The range is represented by the x-axis, while the frequency is represented by the y-axis.

![Capture](https://user-images.githubusercontent.com/37275728/184005703-160ea802-b4e9-49c0-be20-391941e3bcef.PNG)

#### Usecases
* Weight distribution among all people of a particular country.
* Salary distribution among software engineers in a specific city.

### 2. Density Plot

Density plots are essentially smooth histograms. This provides for a more accurate capture of the data's distribution shape. 

![Capture](https://user-images.githubusercontent.com/37275728/184005893-df9c2054-a2d6-4707-969d-57d01fa39887.PNG)

#### Usecases
* Distribution of price of hotel listing.

### 3. Box Plot

A box plot is a graphical representation of the distribution of data. A box plot is usually based on five essential summary statistics:
* The minimum (excluding outliers)
* The first quartile
* The median (or second quartile)
* The third quartile
* The maximum (excluding outliers)

![Capture](https://user-images.githubusercontent.com/37275728/184005970-6f7012c1-4f31-41b3-8f08-6f7bb8e380fa.PNG)

A box plot does not always contain these five figures and therefore, as a norm, a legend should be added with an explanation of what exactly is being shown.

#### Usecases
* Time spent reading across readers.

#### Disadvantages
* The box plot is appropriate for a scientific audience, but is difficult to understand for the general public

## Part-to-whole charts

### 1. Pie Chart

One of the most used methods for displaying part-to-whole is pie chart. A pie chart quickly gives the reader a general idea of the distribution of the total.

![Capture](https://user-images.githubusercontent.com/37275728/184006067-282e5efb-3295-48b6-83a2-29db0b5bd8c1.PNG)

#### Usecases
* Market share of different databases.

#### Disadvantages
* It may be difficult for the readers to compare the individual parts to each other (if that's the emphasis it's better to use bar chart).

### 3. Grouped Bar Chart

A grouped bar chart is also known as a multi-set bar chart. This type of bar chart is employed when two or more data series are presented side by side and categorized on the same axis.

#### Usecases
* Quarterly sales per region.
* Total car sales by producer.

#### Disadvantages
* They get increasingly difficult to read as the number of bars in one group increases.

### 3. Heat Map
A heatmap is a graphical depiction of data that use a color-coding method to represent various values. Heatmaps are effective for cross-referencing multivariate data by arranging variables in rows and columns and coloring cells inside a table.

Heatmaps are excellent for expressing variation across numerous variables, exposing patterns, exhibiting related variables, and discovering relationships between them.

If one of the rows or columns is set to time intervals, heatmaps may also display how data evolves over time. 

#### Usecases
* Average monthly temperatures across the year.
* Departments with the highest amount of attrition over time.

#### Disadvantages
* Heatmaps are better suited for portraying a broader range of numerical data. It is more difficult to distinguish between color hues and retrieve individual data points. 

## Visualize a single value

### 1. Table chart
Table charts are used to present tabular data in a table, as the name implies.

#### Usecases
* Account executive leaderboard
* Registrations per webinar

#### Disadvantages
* Only useful for small datasets.

### 2. Gauge chart

#### Usecases
* Revenue to target
