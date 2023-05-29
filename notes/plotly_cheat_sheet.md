# Plotly Cheatsheet
Plotly is a versatile and interactive data visualization library for Python.

Every dashboard (web app) can be build only with Python. No knowledge of web programming (CSS and JavaScript) is required.

Two things to keep in mind:

* Components (controls): allow you to increase the interactivity of your app.
* Callbacks: actual functions that should be called when some interaction happens.

## Basic Plot Creation

```python
import plotly.express as px

# Create a scatter plot
fig = px.scatter(data, x="x", y="y")

# Create a line plot
fig = px.line(data, x="x", y="y")
```

## Customization

### Title and Axis Labels

```python
fig.update_layout(
    title="My Plot",
    xaxis_title="X-axis",
    yaxis_title="Y-axis"
)
```

### Colors and Markers

```python
fig.update_traces(
    marker=dict(color="red", size=8, symbol="circle"),
    line=dict(color="blue", width=2)
)
```

### Legend and Layout

```python
fig.update_layout(
    legend=dict(
        title="Legend Title",
        x=0.5,
        y=1.0,
        bgcolor="lightgray",
        bordercolor="gray",
        borderwidth=1
    ),
    margin=dict(l=50, r=50, t=50, b=50)
)
```

## Multiple Traces

### Line and Scatter Plots

```python
fig = px.line(data, x="x", y=["y1", "y2"], labels={"variable": "Series"})
fig.add_scatter(x=data["x"], y=data["y3"], mode="lines")
```

### Bar Plot

```python
fig = px.bar(data, x="x", y=["y1", "y2"], barmode="group")
```

### Subplots

```python

from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=2)

fig.add_trace(px.scatter(data, x="x", y="y1").data[0], row=1, col=1)
fig.add_trace(px.line(data, x="x", y="y2").data[0], row=1, col=2)
fig.add_trace(px.bar(data, x="x", y="y3").data[0], row=2, col=1)
fig.add_trace(px.area(data, x="x", y="y4").data[0], row=2, col=2)
```

### 3D Visualization

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Surface(z=data)])
```

## Interactive Features

### Hover Information

```python
fig.update_traces(hovertemplate="x: %{x}<br>y: %{y}")
```

### Click Events

```python
fig.update_layout(clickmode="event+select")
fig.update_traces(selected=dict(marker=dict(color="red")))
```

## Export and Sharing

### Export as HTML or Image

```python
fig.write_html("plot.html")
fig.write_image("plot.png", width=800, height=600)
```

### Online Sharing

```python
import chart_studio.plotly as py

py.plot(fig, filename="plot", auto_open=True)
```

For more details and examples, you can refer to the official Plotly documentation: https://plotly.com/python
