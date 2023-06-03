# Data Visualization Guide and Code Snippets

Welcome! This repository is dedicated to the exploration of various data visualization frameworks through bite-sized code snippets, as well as providing insights on effective data visualization techniques and principles. 

## 🎯 Purpose

The goal of this repository is to serve as a practical guide for understanding the strengths and drawbacks of diverse data visualization frameworks. Additionally, it encompasses my own reflections on the topic of data visualization.

## 📚 Data Sources

Looking for datasets to use for your visualization practices? Here are a few online sources to obtain public datasets:

- [Scikit-Learn Toy Datasets](https://scikit-learn.org/stable/datasets/toy_dataset.html)
- [Tableau Public Data Sets](https://www.tableau.com/learn/articles/free-public-data-sets)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Google Cloud Public Datasets](https://console.cloud.google.com/marketplace/browse?filter=solution-type:dataset)
- [U.S. Government's Open Data](https://data.gov/)
- [Awesome Public Datasets on GitHub](https://github.com/awesomedata/awesome-public-datasets)

## 🛠️ Requirements

Ensure that you have Python 3.8 or above installed to execute the notebooks.

## 🚀 Running Notebooks

To run these notebooks, you have two options:

1. **Online:** You can use the official Jupyter Notebooks online platform without installing anything on your local machine. Try it out here:

    [Jupyter Notebook Demo](https://jupyter.org/try)

2. **Locally:** If you wish to run notebooks on your local machine, follow the steps below:

    - Clone the repository: 
      ```
      git clone https://github.com/djeada/Data-Visualization.git
      ```
    - Navigate to the cloned repository:
      ```
      cd Data-Visualization
      ```
    - Install Jupyter Notebook if you haven't done so already:
      ```
      pip install notebook
      ```
    - Run Jupyter Notebook:
      ```
      jupyter notebook
      ```

## Notes

| # | Description | Notes |
| --- | --- | --- |
| 1 | Introduction to data visualization, including its importance and use cases. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/why_visualize_data.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 2 | Covers the fundamental elements of visual representation in data visualization. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/visual_grammar.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 3 | Explains how to extract and process data for visualization. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/extracting_data.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 4 | Guidance on selecting a visualization framework best suited for your specific use case. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/choosing_framework.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 5 | Quick reference guide and cheat sheet for the Matplotlib data visualization library. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/matplotlib_cheat_sheet.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 6 | Quick reference guide and cheat sheet for the Altair data visualization library. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/altair_cheat_sheet.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 7 | Quick reference guide and cheat sheet for the Plotly data visualization library. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/plotly_cheat_sheet.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 8 | Detailed guide on selecting the appropriate type of plot based on the nature of the data. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/choosing_plot_type.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 9 | In-depth discussion on representing uncertainty in data through error bars. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/error_bars.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 10 | Special topic focusing on creating and interpreting racing charts. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/racing_charts.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 11 | Discusses the ethics of data visualization and how to avoid data misrepresentation. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/data_misrepresentation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |
| 12 | Covers advanced topics on how to create dashboards for presenting multiple visualizations. | <a href="https://github.com/djeada/Data-Visualization/blob/main/notes/dashboards.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a>  |

## Examples

| Description                                                                                                                     | Altair |
|---------------------------------------------------------------------------------------------------------------------------------|------------|
| Plotting a single line, typically the simplest form of data visualization.                                                     | ![single_line](https://github.com/djeada/Data-Visualization/assets/37275728/80fb9cdf-7296-4d48-94fa-da181b78fcb0) |
| Plotting two lines, slightly more complex than a single line.                                                                   | ![two_lines](https://github.com/djeada/Data-Visualization/assets/37275728/6645431b-7b15-4581-ba4b-cf73636093c1) |
| Bar plots represent categorical data with rectangular bars.                                                                     | ![bar_plot](https://github.com/djeada/Data-Visualization/assets/37275728/8334be80-8fb2-476c-81d5-f676892afac8) |
| Pie charts represent proportions or percentages in a whole.                                                                     | [Screenshot](link_to_screenshot) |
| Line charts represent continuous data with lines connecting data points.                                                        | [Screenshot](link_to_screenshot) |
| Histograms display frequency distributions using bins and frequencies.                                                         | [Screenshot](link_to_screenshot) |
| Area charts are similar to line charts but with the area under the line filled in.                                              | ![area_chart](https://github.com/djeada/Data-Visualization/assets/37275728/53b37c60-7323-4823-b896-a0c548f30068) |
| Stacked area charts involve layering multiple datasets.                                                                         | [Screenshot](link_to_screenshot) |
| Grouped bar charts involve grouping bars based on categories.                                                                   | [Screenshot](link_to_screenshot) |
| Box plots show the distribution of data using a five-number summary.                                                            | [Screenshot](link_to_screenshot) |
| Density plots display data distribution using kernel density estimation.                                                       | [Screenshot](link_to_screenshot) |
| Error bar plots show the error or uncertainty associated with data points.                                                      | [Screenshot](link_to_screenshot) |
| Bubble charts represent data using marker size as the third dimension.                                                         | [Screenshot](link_to_screenshot) |
| Correlation heatmaps display complex multi-dimensional data and correlations.                                                   | [Screenshot](link_to_screenshot) |
| Anscombe's Quartet explores datasets with the same statistical properties but different visual appearances.                      | [Screenshot](link_to_screenshot) |

## 📚 Additional Resources

- Scientific-looking matplotlib graphs: [SciencePlots](https://github.com/garrettj403/SciencePlots)
- Cyberpunk style matplotlib graphs: [MPLCyberpunk](https://github.com/dhaitz/mplcyberpunk)

## 📖 References

Find more detailed insights on data visualization from the resources listed below:

- [Introduction to Computational Thinking and Data Science](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/)
- [Storytelling with Data](https://github.com/empathy87/storytelling-with-data)
- [Types of Charts](https://wpdatatables.com/types-of-charts/)
- [Uncertainty in Visualization](https://advait.org/files/sarkar_2015_uncertainty_vis.pdf)
- [Data Visualization: A Practical Introduction](https://clauswilke.com/dataviz/index.html)
- [Matplotlib CheatSheets](https://github.com/matplotlib/cheatsheets)
- [Styling with Matplotlib](https://jonchar.net/notebooks/matplotlib-styling/)

## 🙏 Contributing

Contributions are warmly welcomed. If you are considering large changes, please open an issue first to discuss your ideas. Remember to update tests as required for your changes.

## 📄 License

This project is licensed under the terms of the [MIT license](https://choosealicense.com/licenses/mit/).
