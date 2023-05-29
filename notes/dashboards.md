## Dashboards in Data Visualization

A dashboard is a visual representation that succinctly displays pertinent data. Composed of numerous plots and controls, dashboards are frequently linked to APIs or databases from which data is fetched. The range of data visualization techniques spans from basic plots to complex dashboards, and the choice between these depends on the scope of the data and the intended interaction level.

## Dashboards vs. Simple Plots

Both dashboards and simple plots serve the purpose of visualizing data, but their applications and complexities vary significantly.

* For creating simple plots, tools as basic as Excel might suffice, and you don't necessarily need a programming language. On the other hand, dashboards, being more comprehensive, often require the construction of an entire application, hence necessitating more work.
* Dashboards enable more dense data packing. For example, if you have data spanning over years, you can present it on plots specific to a certain year and permit users to switch between years using a control. However, if your data isn't extensive, a basic plot may be sufficient.
* Dashboards empower users to explore the entire dataset easily, enabling the identification of data outliers and correlations. Dashboards convey extensive information that would otherwise be time-consuming to extract from a simple plot.

## Designing Dashboards

When designing a dashboard, you have a multitude of factors to consider. These include connecting it with an API or a database, simplifying the dashboard by reducing the number of plots and controls, and handling data processing (either offline pre-processing to pre-assemble the data or online processing in dedicated servers and designing an API).

One crucial factor to remember is to keep the dashboard as simple and intuitive as possible. Although a dashboard with fewer plots and controls might be adequate, it's crucial to analyze why such complexity was necessary in the first place. However, simplifying a dashboard may entail storing new series or tables, leading to potential data management issues.

## Dashboarding Libraries in Python

Python offers several libraries to create interactive dashboards, including Dash, Bokeh, Streamlit, Panel, and Voila. These libraries vary in their ease of use, customizability, interactivity, data handling capabilities, and deployment options.

### Dash

Dash, created by the same team behind Plotly, is a Python framework for building analytical web applications.

**Pros:**

* It integrates well with Plotly, allowing you to create highly interactive visualizations.
* It has no JavaScript required for creating interactive applications.
* It's designed for data science and ML teams to make web applications.

**Cons:**

* It might require more boilerplate code compared to other options.
* Dash apps can be slow with larger datasets.

### Bokeh

Bokeh is a Python interactive visualization library that targets modern web browsers for presentation.

**Pros:**

* It supports creating dashboards directly from Jupyter Notebooks using the Bokeh server.
* It has excellent interactive capabilities.

**Cons:**

* The learning curve might be steep for beginners.
* Community support is not as strong compared to other libraries.

### Streamlit

Streamlit is a fast and easy way to create data applications.

**Pros:**

* It allows rapid prototyping and iteration.
* It has a minimal and intuitive API.
* It requires less boilerplate code compared to Dash and Bokeh.

**Cons:**

* It offers limited layout options.
* It's newer than other libraries, so the community is still growing.

### Panel

Panel is a high-level app and dashboarding solution for Python.

**Pros:**

* It supports a wide range of visualizations from many different libraries.
* It integrates well with the PyViz ecosystem (Bokeh, Datashader, etc.)

**Cons:**

* The design options may seem limited compared to other options.
* Its focus on notebook-based development might not fit all use-cases.

### Voila

Voila turns Jupyter notebooks into standalone web applications.

**Pros:**

* It allows creating dashboards directly from Jupyter Notebooks.
* It integrates well with Jupyter widgets to create interactive elements.

**Cons:**

* It is largely tied to Jupyter, which may not suit all workflows.
* It has less flexibility in terms of design and layout compared to some other libraries.

## Examples

For some real-world dashboard examples, visit [this link](https://www.other-levels.com/collections/all-products).
