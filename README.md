# Temperature Analysis with Python

This project analyzes a simple temperature dataset using Python.

The data is loaded from a CSV file, basic statistics are calculated, and the results are visualized with a line chart.

## Features

- Loads data from a CSV file
- Displays the first rows of the dataset
- Calculates:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Day with the highest temperature
- Creates a temperature chart using matplotlib

## Technologies

- Python
- pandas
- matplotlib

## Project structure

```text
temperature-analyse/
├── main.py
├── temperature_data.csv
├── temperature_plot.png
├── README.md
└── requirements.txt
```

## How to run

pip install -r requirements.txt
python main.py

## Output

The program prints basic statistics in the terminal and generates a temperature chart.

Example results:

Average temperature: 20.8
Maximum temperature: 27
Minimum temperature: 15
Day with highest temperature: 10
Chart

Learning goals

This project helped me practice:

Reading CSV files with pandas
Selecting columns from a dataset
Performing basic data analysis
Creating visualizations with matplotlib