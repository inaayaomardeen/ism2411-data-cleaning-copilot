# ISM2411 – Data Cleaning with GitHub Copilot

This Github Repository assignment contains a small, GitHub-ready Python project created for my Python for Business course. The purpose of this project was to clean a messy sales dataset
using Python and pandas, while demonstrating responsible use of GitHub Copilot to maintain acadmeic and professional integrity.

# Project Overview
The project loads a raw CSV file containing sales data, applies a series of
data cleaning steps, and writes a cleaned version of the dataset to a new CSV file. The code is organized into reusable functions to make the code easier to test and understand. 
All cleaning is done in Python.

# Cleaning Steps 
This assignment performs the following data cleaning actions:
- Loads the raw sales data from a CSV file and validates that the file exists
- It standardizes column names by removing whitespace, converting to lowercase,
and replacing spaces with underscores
- Strips leading and trailing whitespace from product- and category-related
text fields
- Converts price and quantity columns to numeric values
- Drops rows with missing critical numeric values
- Removes rows containing negative prices or quantities, which are treated as
data entry errors
- Writes the cleaned dataset to `data/processed/sales_data_clean.csv`