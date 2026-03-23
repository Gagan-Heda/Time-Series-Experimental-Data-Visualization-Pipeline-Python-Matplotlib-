# Time-Series Experimental Data Visualization Pipeline (Python + Matplotlib)

Python-based command-line pipeline for visualizing time-series experimental data. Supports plotting single or multiple datasets, handling replicates, and displaying statistical summaries such as mean trends and standard deviation error bars.

---

## Overview

This project provides a reproducible workflow to generate publication-quality plots from experimental time-series data. The pipeline reads input files containing measurements over time and produces clear visualizations of trends under different experimental conditions.

Each input file contains:

- A header specifying the experimental condition  
- Time-series measurements (single values or replicates)  

The tool progresses from simple line plotting to advanced visualizations with error bars and multi-dataset comparisons.

---

## Objectives

- Generate line plots for individual datasets  
- Visualize multiple experimental conditions together  
- Handle replicate measurements and calculate statistical summaries  
- Automate plotting through a command-line interface  
- Save high-quality figures in PNG format  

---

## Key Features

### Single Dataset Plotting

- Reads a single input file of time and measurements  
- Generates a basic line plot with Matplotlib  
- Saves output as a PNG image  

---

### Axis Labels and Legend

- Adds meaningful labels:
  - X-axis: time  
  - Y-axis: measurement (e.g., cell count)  
- Automatically generates legends based on dataset name  
- Uses intelligent placement for clarity (`loc='best'`)  

---

### Multi-Dataset Plotting

- Accepts multiple input files simultaneously  
- Plots each dataset as a distinct line  
- Enables comparison across experimental conditions  

---

### Replicate Handling and Statistics

- Supports multiple measurements per time point  
- Computes mean and standard deviation across replicates  
- Plots:
  - Mean trends as line plots  
  - Error bars representing variability  

---

### Flexible Command-Line Interface

- Accepts arbitrary number of input files using `sys.argv`  
- Fully automatable for batch plotting  

---

## Input Format

### Single Measurement per Timepoint
Condition A
0,72
20,71
40,77


### Multiple Replicates per Timepoint
Condition A
0,72,39,16,62
20,71,45,17,67
40,77,51,21,77


---

## Technologies

- Python  
- Matplotlib  
- NumPy  
- sys (command-line argument parsing)  

---

## Implementation Details

- Uses `matplotlib.use('Agg')` for headless plotting  
- Parses input files with Python file I/O  
- Computes statistics (mean, standard deviation) using NumPy  
- Generates consistent and reproducible plots  

---

## Output

- PNG images displaying:
  - Time vs measurement  
  - Multiple experimental conditions side-by-side  
  - Mean trends with standard deviation error bars  

---

## Skills Demonstrated

- Data visualization in Python  
- Command-line interface (CLI) design  
- Input file parsing and processing  
- Statistical analysis of replicates  
- Dynamic handling of multiple datasets  
- Reproducible figure generation  

---

## Notes

- Plots are designed to closely match reference outputs  
- Error bars reflect variability across replicates  
- Minor visual differences may occur depending on environment  

---

## Author

**Gagan Heda**
