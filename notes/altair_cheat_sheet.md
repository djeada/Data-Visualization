## Altair Cheatsheet

Altair is a declarative statistical visualization library for Python, based on the Vega-Lite specification.

## Basic Chart Creation

```python
import altair as alt

# Create a basic line chart
alt.Chart(data).mark_line().encode(
    x='x',
    y='y'
)

# Create a scatter plot
alt.Chart(data).mark_circle().encode(
    x='x',
    y='y'
)
```

## Data Encoding

### Position Encoding

```python

alt.Chart(data).mark_point().encode(
    x='x',
    y='y'
)

alt.Chart(data).mark_bar().encode(
    x='x',
    y='y'
)
```

### Color Encoding

```python

alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    color='category'
)

alt.Chart(data).mark_bar().encode(
    x='x',
    y='y',
    color=alt.condition(
        alt.datum.y > 0,
        alt.value('red'),
        alt.value('blue')
    )
)
```

### Size Encoding

```python

alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    size='magnitude'
)
```

### Shape Encoding

```python
alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    shape='category'
)
```

## Aggregation and Grouping

### Aggregation

```python
alt.Chart(data).mark_bar().encode(
    x='category',
    y='average(value)'
)

alt.Chart(data).mark_line().encode(
    x='year',
    y='average(value)',
    color='category'
)
```

### Grouping

```python
alt.Chart(data).mark_bar().encode(
    x='category',
    y='average(value)',
    column='year'
)

alt.Chart(data).mark_line().encode(
    x='x',
    y='y',
    color='category',
    row='year'
)
```

## Interaction and Selection

### Tooltip

```python
alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    tooltip=['x', 'y']
)
```

## Selection

```python
selection = alt.selection_multi(fields=['category'])
color = alt.condition(selection, 'category:N', alt.value('lightgray'))

alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    color=color
).add_selection(selection)
```

## Composition and Layering

### Composition

```python
chart1 = alt.Chart(data1).mark_line().encode(
    x='x',
    y='y'
)

chart2 = alt.Chart(data2).mark_circle().encode(
    x='x',
    y='y'
)

chart1 | chart2
```

### Layering

```python
chart1 = alt.Chart(data1).mark_line().encode(
    x='x',
    y='y'
)

chart2 = alt.Chart(data2).mark_circle().encode(
    x='x',
    y='y'
)

chart1 + chart2
```

## Configuration and Styling

### Chart Configuration

```python
alt.Chart(data).properties(
    title='My Chart',
    width=400,
    height=300
)
```

### Axis Configuration

```python
alt.Chart(data).mark_point().encode(
    x=alt.X('x', axis=alt.Axis(title='X-Axis')),
    y=alt.Y('y', axis=alt.Axis(title='Y-Axis'))
)
```

### Legend Configuration

```python
alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    color='category',
    shape='category',
    size='magnitude'
).configure_legend(
    title='Legend Title',
    orient='top-right',
    labelLimit=100
)
```

For more details and examples, you can refer to the official Altair documentation: https://altair-viz.github.io
