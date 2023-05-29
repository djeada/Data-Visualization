## Data Misrepresentation

### Fake Data
- Some people alter the data itself rather than simply the representation. Always check the source of the data.
- Even partially incorrect data can be misleading. Essential data points may be omitted during data preparation and filtering, significantly altering the results.

### Misleading Scales and Axis
- The expectation for the y and x axes is to begin at zero. Minor differences between data points may be exaggerated by adjusting the y-axis starting point.
- Different scales can be used for each axis, potentially leading to misinterpretations. Make sure that the scale choice aligns with the data and doesn't distort the perception.

#### Category Axis
- On a category axis, values are shown at a consistent distance from one another, regardless of the value category.
- Categories can be text as well as numbers, offering flexibility but also potential for misinterpretation if not clearly labeled.

#### Linear Axis
- A linear axis distributes values based on a starting value, an ending value, and a number of steps.
- Ensuring the steps are consistent and align with the data intervals can be critical for correct data representation.

#### Logarithmic Axis
- On a logarithmic axis, each step has a value that is a factor larger than the previous one.
- While useful for certain data types, it's important to label this axis clearly to avoid misinterpretation.

### Cherry-Picking Data
- Selectively presenting or ignoring certain subsets of your data can lead to misrepresentation of the overall scenario.
- Strive to consider all relevant data when creating visualizations and avoid selective data presentation.

### Biased Color Schemes
- The use of color can heavily influence interpretations of visualizations.
- Beware of color schemes that over-emphasize certain sections of the data or under-represent others, as this can cause misinterpretation.

### Overloading Information
- Overloading a visualization with too much information can confuse the audience and obscure the actual insights.
- Strive for simplicity and clarity in your visualizations. When in doubt, it may be better to create multiple simple graphs rather than one overly complex one.

### Misleading Representation
- The type of visualization used can also misrepresent data.
- Always make sure the type of data matches the chosen style of visualization. For example, a pie chart for time-series data is inappropriate and misleading.

### Improper Use of Area
- Our perception naturally interprets area in two dimensions, which can lead to misinterpretations when representing quantities with area.
- If the dimensions of a shape in a graph (such as a circle or a square) are doubled, the area increases fourfold. Make sure your visualization doesn't exaggerate differences due to this effect.

### Ignoring Marginal Effects and Interactions
- Ignoring or failing to accurately represent interaction effects and marginal changes can result in misleading visualizations.
- Context is key, and you should always consider the interaction among variables.

### Misrepresenting Uncertainty
- Visualizations often represent estimates, but many fail to convey the degree of uncertainty around these estimates.
- Avoid creating an illusion of precision that isn't justified by the data. Always display error bars, confidence intervals, or other indicators of uncertainty where applicable.

### Neglecting to Normalize
- It's important to normalize data when making comparisons, to account for differences in population size or other relevant factors.
- Always check if normalization is needed for your data. Failure to normalize can lead to incorrect comparisons and conclusions.

### The Lie Factor
- A single number, known as the Lie Factor, can describe the relationship between the magnitude of the effect in the data representation and the size of the effect in the data source.
- The Lie Factor was defined in Edward Tufte's book "The Visual Display of Quantitative Information" in 1983 as the size of effect in the graphic divided by the size of effect in the data.
- The size of effect is calculated as the absolute value of the difference between the last and first value divided by the first value.

$$ Lie\ Factor = \frac{size\ of\ effect\ in\ graphic}{size\ of\ effect\ in\ data} $$

$$ size\ of\ effect =  \frac{\vert\ {last\ value}-{first\ value}\ \vert}{first\ value} $$

## Literature
- "How to Lie with Statistics" is a book written by Darrel Huff in 1954, providing many still-relevant examples of data misrepresentation.
    - Choosing the arithmetic average as the "middle" instead of the median.
    - Tampering with the scales.
    - Visualizing a factor of 2 as a much larger difference.
