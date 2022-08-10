## Fake data
Some people alter the data itself rather than simply the representation, therefore always check the source of data.

Data does not have to be fully made up to be fake! Some essential data points may be omitted during the data preparation and filtering procedure, which drastically changes the results.

## Truncatnating y-axis

People expect the y and x axes to begin at zero. If there are minor differences between data points, we may adjust the y-axis starting point to make them more apparent. That is how little fluctuations can appear to be enormous. Everything is true in theory, but readers who are not properly trained in statistics are easily confused.

## Varying the axes in graphs
People are expecting that the x and y axes will be scaled in the same manner. We could, in fact, use various scales for each axis. 

### Category axis
Values on a category axis are shown at a constant distance from one another, independent of the value category. Categries don't have to be numbers, they can be text also.

### Linear axis
On a linear axis, values are distributed based on a beginning value, an end value, and a number of steps.

### Logarithmic axis
Each step on a logarithmic axis has a value that is a factor bigger than the preceding step. If the multiplication factor is ten, then each step is 10 times greater than the previous one (10, 100, 1000...)

## The Lie Factor

We can find a single number that describes the relationship between the magnitude of the impact in the data representation and the size of the effect in the source data.
In 1983, Edward Tufte's book "The Visual Display of Quantitative Information" defined the Lie Factor.

$$ Lie\ Factor = \frac{size\ of\ effect\ in\ graphic}{size\ of\ effect\ in\ data} $$

$$ size\ of\ effect =  \frac{\vert\ {last\ value}-{first\ value}\ \vert}{first\ value} $$
