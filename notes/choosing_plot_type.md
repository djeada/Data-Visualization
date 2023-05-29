## Choosing Plot Type

Data visualization plays a critical role at various stages in the data science process. In the initial stages, it provides preliminary insights into an unfamiliar dataset. After the data has been gathered, analyzed, and modeled, visualizations help illustrate relationships and facilitate the drawing of conclusions. It serves as a tool for communicating insights through visually expressive elements like graphs, charts, maps, and diagrams, simplifying complex data interpretation, pattern discovery, trend identification, and predictive analysis.

Each plot type has its own set of advantages and disadvantages, necessitating a careful selection process. Consider the following questions before deciding:

- What do you want to emphasize or illustrate (quantities, trends, correlations, geographic insights)?
- Which visualization makes the data as easy to read and analyze as possible?
- What is the conventional technique for displaying data in your field to avoid potential confusion?
- Does the visualization maintain its clarity in black and white (for printing purposes)?

Let's explore various types of graphs and charts, grouped by their purpose:

## Visualizing Relationships

Visualizing relationships involves demonstrating a connection or correlation between two or more variables.

### 1. Bar Chart

Bar charts effectively display quantities of various item types at a specific time point. One axis of the chart represents the categories being compared, while the other signifies a measured value.

![Bar Chart Example](https://user-images.githubusercontent.com/37275728/184005258-9f3884b8-3ed5-49d1-8b44-2b760e6fc1b6.PNG)

**Usecases:**
- Comparing revenue across different areas.
- Analyzing sales performance for different products.

**Disadvantages:**
- Not effective for investigating time patterns or categorical data.
- Limited to comparing a single category of data to individual sub-items.

### 2. Scatter Plot

A scatter plot is a widely used graph in scientific research, comprising several data points plotted on two axes.

![Scatter Plot Example](https://user-images.githubusercontent.com/37275728/184005392-a9576de8-6175-4c88-a297-d7b6e1e86f2d.PNG)

**Usecases:**
- Displaying the relationship between GPA and initial salary.
- Analyzing the correlation between advertising spending and sales.

**Disadvantages:**
- Not effective for investigating time patterns or categorical data.
- Can become cluttered with a large number of data points.

### 3. Bubble Chart

Bubble charts are employed when illustrating three variables simultaneously. One variable is represented on the x-axis, another on the y-axis, and the third as the size of the bubble.

**Usecases:**
- Demonstrating the relationship between life expectancy, per capita GDP, and population size.
- Analyzing the correlation between temperature, humidity, and crop yield.

**Disadvantages:**
- Limited to visualizing three variables only.
- Bubble size can sometimes make it difficult to accurately compare data points.

## Visualizing Data Over Time

In certain scenarios, the existence of a relationship between variables isn't sufficient; further analysis to visualize when the relationship occurred can be beneficial. This style of visualization presents data across time to identify patterns.

### 1. Line Chart

Line charts depict quantitative values over time and are created by connecting data points on a Cartesian coordinate grid. The y-axis usually has a numerical value, while the x-axis represents a timeframe or a series of intervals. The orientation of the graph's line can indicate patterns in variable changes.

**Usecases:**
- Visualizing revenue, energy consumption, or Google searches over time.
- Tracking stock prices and identifying trends.

### 2. Area Chart

An area chart builds upon the concept of a line chart. The colored area signifies the distribution of the total value over time. These charts are excellent for showcasing changes between two or more data points.

**Usecases:**
- Visualizing total sales or active users over time.
- Analyzing the distribution of website traffic throughout the day.

**Disadvantages:**
- Not ideal for displaying fluctuating values or comparing exact values of two (or more) areas at a specific time.
- Can obscure smaller fluctuations due to the area filling.

### 3. Stack Area Chart

A stack area chart is an extension of an area chart, showing the values of multiple groups on a single graph with group values stacked on top of each other.

![Stack Area Chart Example](https://user-images.githubusercontent.com/37275728/184005506-e11296cb-a330-4def-b193-cdb4e57b1c6d.PNG)

**Usecases:**
- Visualizing active users over time by segment or total revenue over time by country.
- Analyzing the distribution of expenses across different categories over time.

**Disadvantages:**
- Only display whole integers, cannot display negative values.
- Can become visually cluttered when there are too many stacked categories.

## Distribution Plots

Distribution plots illustrate the sample data distribution by comparing the empirical distribution of the data to theoretical values. These charts can be used in addition to formal hypothesis testing to assess if the sample data could be represented by a specific distribution.

### 1. Histogram

A histogram displays the distribution of a variable by showing the frequency of data points falling within a specific range.

![Histogram Example](https://user-images.githubusercontent.com/37275728/184005703-160ea802-b4e9-49c0-be20-391941e3bcef.PNG)

**Usecases:**
- Visualizing the average temperature or salary distribution in a specific city.
- Analyzing the distribution of test scores in a classroom.

**Disadvantages:**
- Bin size selection can impact the interpretation of the distribution.
- Not suitable for displaying individual data points.

### 2. Density Plot

Density plots are essentially smooth histograms, providing a more accurate capture of the data's distribution shape.

![Density Plot Example](https://user-images.githubusercontent.com/37275728/184005893-df9c2054-a2d6-4707-969d-57d01fa39887.PNG)

**Usecases:**
- Visualizing the distribution of hotel listing prices.
- Analyzing the distribution of income levels in a population.

**Disadvantages:**
- Can be computationally intensive for large datasets.
- Interpretation may be subjective due to smoothing techniques.

### 3. Box Plot

A box plot is a graphical representation of the data distribution, with a box representing the middle 50% of values, the top 25% above the box, and the bottom 25% below the box. Outliers are shown outside the box area.

![Box Plot Example](https://user-images.githubusercontent.com/37275728/184005970-6f7012c1-4f31-41b3-8f08-6f7bb8e380fa.PNG)

**Usecases:**
- Visualizing the time spent reading across readers.
- Analyzing the distribution of product ratings across different categories.

**Disadvantages:**
- Can be challenging to understand for a non-scientific audience.
- Limited information about the shape of the distribution.

## Part-to-Whole Charts

### 1. Pie Chart

Pie charts are commonly used to represent part-to-whole distributions. They give readers a quick understanding of the overall distribution.

![Pie Chart Example](https://user-images.githubusercontent.com/37275728/184006067-282e5efb-3295-48b6-83a2-29db0b5bd8c1.PNG)

**Usecases:**
- Visualizing the market share of different databases.
- Analyzing the composition of a company's expenses.

**Disadvantages:**
- Comparing individual parts to each other can be challenging for readers.
- Difficult to accurately interpret small differences between sections.

### 2. Grouped Bar Chart

A grouped bar chart, also known as a multi-set bar chart, is used when two or more data series are presented side-by-side and categorized on the same axis.

**Usecases:**
- Visualizing quarterly sales per region or total car sales by producer.
- Comparing the performance of different products across different months.

**Disadvantages:**
- The readability decreases as the number of bars in one group increases.
- Not suitable for displaying large datasets.

### 3. Heat Map

A heatmap is a graphical representation of data that uses a color-coding system to represent different values. Heatmaps are excellent for expressing variation across several variables, uncovering patterns, displaying related variables, and revealing relationships between them.

**Usecases:**
- Visualizing the average monthly temperatures across the year or departments with the highest attrition rate over time.
- Analyzing customer engagement across different products and time periods.

**Disadvantages:**
- Heatmaps are better for broader numerical data ranges, but individual data points can be hard to distinguish due to color hues.
- Not suitable for displaying textual or categorical data.

## Single Value Visualization

### 1. Table Chart

As the name suggests, table charts are used to present tabular data.

**Usecases:**
- Visualizing an account executive leaderboard or registrations per webinar.
- Displaying summary statistics for different categories.

**Disadvantages:**
- Suitable only for small datasets.
- Not effective for displaying trends or patterns.

### 2. Gauge Chart

Gauge charts are used to visualize a single key performance indicator (KPI) or metric.

**Usecases:**
- Visualizing revenue to target.
- Displaying customer satisfaction scores.

**Disadvantages:**
- Can be visually limited in terms of information conveyed.
- Not suitable for displaying complex data relationships.

