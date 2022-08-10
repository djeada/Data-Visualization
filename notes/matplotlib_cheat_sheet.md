## Matplotlib terminology

A figure contains the window in which plotting takes place.

![matplotlib](https://user-images.githubusercontent.com/37275728/179934086-bf826c5a-8e8e-4dc1-ba41-33ea6ca26f77.png)

A plot is often represented by axes. Each Axis contains an x- and y-axis for plotting, as well as a title, an x-label, and a y-label.

Ticks are data point markers on axes, or the values used to show specific points on the coordinate axis. These values can be either numbers or strings. The axes adjust and take the default ticks whenever we plot a graph. Matplotlib's default ticks are typically adequate in most scenarios, although they are not perfect for every plot.

A graph's spine is the same as graph's edge. The axis tick markers are shown directly below it and it is also indicating the plotting area borders.

Pyplot is a Matplotlib module that offers basic utilities for adding plot components like as lines, pictures, text, and so on to the selected axes in the selected figure.

Let's take a look at some examples:

1. Draw a figure and an axis with a single line:

```python
import matplotlib.pyplot as plt

# create figure
fig = plt.figure()

# create axis
ax = fig.add_subplot(111)

# create line
ax.plot([1,2,3,4,5,6,7,8,9,10])

# show figure
plt.show()
```


2. Instead of creating new figures to add additional lines, we may reuse the same figure we have created:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# create line
ax.plot([1,2,3,4,5,6,7,8,9,10])

# create second line
ax.plot([1,4,9,16,25,36,49,64,81,100])

# show figure
plt.show()
```

3. We can also have several axes:

```python
import matplotlib.pyplot as plt

fig = plt.figure()

# add first subplot in layout that has 1 row and 2 columns
ax1 = fig.add_subplot(121)

# add second subplot in layout that has 1 row and 2 columns
ax2 = fig.add_subplot(122)

# create line
ax1.plot([1,2,3,4,5,6,7,8,9,10])

# create second line
ax2.plot([1,4,9,16,25,36,49,64,81,100])

# show figure
plt.show()
```

4. The most basic plot configuration involves adding titles, labels, legends, and scaling axes:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1,2,3,4,5,6,7,8,9,10])

# add title
ax.set_title('My Plot')

# add x-label
ax.set_xlabel('x-axis')

# add y-label
ax.set_ylabel('y-axis')

# add legend
ax.legend(['My Plot'])

# show figure
plt.show()
```

Matplotlib performs a good job at selecting default axis bounds for our plot, but it's occasionally nice to have more control. The xlim() and ylim() are used most commonly:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1,2,3,4,5,6,7,8,9,10])

# set x-axis limits
ax.set_xlim(-5, 5)

# set y-axis limits
ax.set_ylim(-5, 5)

# show figure
plt.show()
```

## Hiding Ticks or Labels

Perhaps the most common tick/label formatting operation is the act of hiding ticks or labels. This can be done using plt.NullLocator() and plt.NullFormatter(), as shown here:

```python
ax = plt.axes()
ax.plot(np.random.rand(50))

ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())
```

Particularly for the x ticks, the numbers nearly overlap and make them quite difficult to decipher. We can fix this with the plt.MaxNLocator(), which allows us to specify the maximum number of ticks that will be displayed. Given this maximum number, Matplotlib will use internal logic to choose the particular tick locations:

```python
# For every axis, set the x and y major locator
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(3))
    axi.yaxis.set_major_locator(plt.MaxNLocator(3))
```

## Colors and styles

Matplotlib contains an amazing number of options for setting graph visuals. However, these configurations are not always simple or intuitive.

You may make your own style or use one of the premade styles. For instance, in this case, we will apply the seaborn style to the plot:

```python
plt.style.use('seaborn')
```

To see all available sytles use:
    
```python
print(plt.style.available)
```

For figures used within presentations, it is often useful to have a dark rather than light background. The dark_background style provides this:

with plt.style.context('dark_background'):
    hist_and_lines()


*Bayesian Methods for Hackers( style

There is a very nice short online book called Probabilistic Programming and Bayesian Methods for Hackers; it features figures created with Matplotlib, and uses a nice set of rc parameters to create a consistent and visually-appealing style throughout the book. This style is reproduced in the bmh stylesheet:

with plt.style.context('bmh'):
    hist_and_lines()


The ggplot package in the R language is a very popular visualization tool. Matplotlib's ggplot style mimics the default styles from that package:

```python

with plt.style.context('ggplot'):
    hist_and_lines()
```


We can adjust this by hand to make it a much more visually pleasing plot:

```python

# use a gray background
ax = plt.axes(axisbg='#E6E6E6')
ax.set_axisbelow(True)

# draw solid white grid lines
plt.grid(color='w', linestyle='solid')

# hide axis spines
for spine in ax.spines.values():
    spine.set_visible(False)
    
# hide top and right ticks
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# lighten ticks and labels
ax.tick_params(colors='gray', direction='out')
for tick in ax.get_xticklabels():
    tick.set_color('gray')
for tick in ax.get_yticklabels():
    tick.set_color('gray')
    
# control face and edge color of histogram
ax.hist(x, edgecolor='#E6E6E6', color='#EE6666');
```



Changing the Defaults: rcParams

Each time Matplotlib loads, it defines a runtime configuration (rc) containing the default styles for every plot element you create. This configuration can be adjusted at any time using the plt.rc convenience routine. Let's see what it looks like to modify the rc parameters so that our default plot will look similar to what we did before.

We'll start by saving a copy of the current rcParams dictionary, so we can easily reset these changes in the current session:

IPython_default = plt.rcParams.copy()

Now we can use the plt.rc function to change some of these settings:

from matplotlib import cycler
colors = cycler('color',
                ['#EE6666', '#3388BB', '#9988DD',
                 '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)

With these settings defined, we can now create a plot and see our settings in action:


## Text and annotations

Sometimes text and labels may provide us with additional explanations or simply point our attention in a correct direction. The <code>ax.text()</code> function accepts an <code>x</code> location, a <code>y</code> position, a string, and optional keywords that control the text's color, size, style, alignment, and other features.

Another useful function is <code>plt.annotate()</code>, it can be used to display text and an arrow pointing to that text. 

## Types of plots

There are various plots which can be created using python Matplotlib. We will discuss the most used plots for data visualization in this section.

### Scatter plot

```python
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,4,9,16,25,36,49,64,81,100]
plt.scatter(x, y, label='Scatter Plot', color='r', marker='*')
plt.show()
```

### 3D scatter plot

```python
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,4,9,16,25,36,49,64,81,100]
z = [1,8,27,64,125,216,343,512,729,1000]
plt.scatter(x, y, z, label='Scatter Plot', color='r', marker='*')
plt.show()
```

### Histogram

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
plt.hist(x, bins=10, label='Histogram')
plt.show()
```

### Pie chart

```python
import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()
```

### Bar chart

```python
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,4,9,16,25,36,49,64,81,100]
plt.bar(x, y, label='Bar Plot', color='lightblue')
plt.show()
```

### Area chart

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y_a = np.abs(np.random.randn(10))
y_b = np.abs(np.random.randn(10))
plt.fill_between(x, y_a, label='Area Chart', color='lightblue')
plt.fill_between(x, y_b, label='Area Chart', color='lightgreen')
plt.show()
```

### Box plot

     Q1-1.5IQR   Q1   median  Q3   Q3+1.5IQR
                  |-----:-----|
         |--------|     :     |--------|    o  o
                  |-----:-----|
                  <----------->            fliers
                       IQR

An example:

```python
import matplotlib.pyplot as plt

fig = plt.figure()

x1 = [-0.46, -1.25, -2.62, 0.22]
x2 = [0.24, 1.88, -0.49, -0.73, -0.49]
x3 = [-0.44, 0.93, 0.19, -4.36, -0.88]

plt.boxplot([x for x in [x1, x2, x3]], 0, "lightblue", 1)
plt.show()
```
