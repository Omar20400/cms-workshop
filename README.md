# CMS Workshop

A complete collection of Jupyter notebooks, Python scripts, and data files created during the CMS Workshop. This repository covers Python fundamentals, file parsing, processing multiple files, tabular data analysis, data visualization, and writing reusable functions.

## Repository Structure

### Jupyter Notebooks (Lessons)

- **Lesson1.ipynb** — Introduction to Python fundamentals, including variables, data types, and basic operations.
- **lesson2_file_parsing.ipynb.ipynb** — Reading and parsing data files using Python (working with text files and extracting information).
- **lesson3 Processing Multiple Files and Writing Files.ipynb** — Looping over multiple files, processing their content, and writing results to output files.
- **lesson4 Working with Tabular Data.ipynb** — Working with tabular data, likely using libraries such as NumPy and Pandas.
- **Lesson 5 Plotting and Data Visualization.ipynb** — Data visualization using Matplotlib: line plots, markers, legends, subplots, and saving figures.
- **Lesson 6 Writing Functions.ipynb** — Writing reusable and modular Python functions.

### Folders

- **chemistry_project/** — A chemistry analysis project that measures distances between atoms, identifies bonds, and outputs bond lengths.
- **data/** — Data files used throughout the notebooks (e.g., `distance_data_headers.csv`).

### Data Files

- **energies.txt** — Sample data file containing energy values, used in file parsing lessons.
- **file_name.txt** — Sample text file used for practicing file parsing.

### Generated Plots (PNG)

The following plots were generated during Lesson 5 (Plotting and Data Visualization):

- **THR4_ATP.png** — Distance between THR4 and ATP over simulation frames.
- **THR4_ASP.png** — Distance between THR4 and ASP over simulation frames.
- **TYR6_ATP.png** — Distance between TYR6 and ATP over simulation frames.
- **TYR6_ASP.png** — Distance between TYR6 and ASP over simulation frames.
- **all_samples.png** — All distance measurements plotted together.
- **distance_plot.png** — Combined distance plot with legend.
- **distance_subplots.png** — Subplots comparing distance measurements.
- **two_samples.png** — Comparison of two selected samples.

### Other Files

- **.gitignore** — Specifies which files and folders Git should ignore (e.g., Jupyter checkpoint cache files).
- **README.md** — This file.

## Lesson 5 Details — Plotting and Data Visualization

Lesson 5 uses a CSV file (`data/distance_data_headers.csv`) containing molecular dynamics simulation data with the following columns:

- `Frame` — Simulation frame number.
- `THR4_ATP` — Distance between THR4 and ATP.
- `THR4_ASP` — Distance between THR4 and ASP.
- `TYR6_ATP` — Distance between TYR6 and ATP.
- `TYR6_ASP` — Distance between TYR6 and ASP.

The notebook demonstrates:

- Loading CSV data using `numpy.genfromtxt`.
- Separating headers from numerical data.
- Plotting line graphs with Matplotlib (`plt.plot`).
- Adding axis labels, titles, and legends.
- Using markers (`marker='o'`) and different line styles.
- Saving figures with `plt.savefig` at high resolution (`dpi=300`).
- Creating subplots using `plt.subplots`.
- Looping over data columns to generate multiple plots automatically.
- Setting axis limits with `plt.ylim`.

## Requirements

To run the notebooks, you need:

- Python 3
- NumPy
- Matplotlib
- Jupyter Notebook or JupyterLab

## Author

- **Omar** — GitHub: [@Omar20400](https://github.com/Omar20400)