"""
Data cleaning script for ISM2411.

This script loads the raw sales CSV, cleans the data and saves a cleaned version.
"""

import os 
import pandas as pd 

#function to load the raw sales dataset from a CSV file. 
#I am separating this so it is easier to test and reuse.
def load_data(file_path:str):
    """Load the raw sales data from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    df = pd.read_csv(file_path)
    return df

#Function to clean and standardize column names.
#This ensures consistency: lowercase, underscores and no extra spaces.
def clean_column_names(df):
    """Standardize column names and strip whitespaces from text fields."""

    cleaned_df = df.copy()

    #Standardize column names: lowercase, no spaces.
    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ","_")
    )

    #Strip whitespaces from product/category columns if they exist
    text_columns = ["product", "product_name", "category"]
    for col in text_columns: 
        if col in cleaned_df.columns:
            cleaned_df[col] = cleaned_df[col].astype(str).str.strip()

    return cleaned_df

#Function to handle missing prices and quantities.
# I am converting them to numeric and drop rows with missing values.
def handle_missing_values(df) :
    """Convert price/quantiy columns to numeric and drop missing values."""

    cleaned_df = df.copy()

    #FInd price and quantity columns by their names
    price_cols = [c for c in cleaned_df.columns if "price" in c]
    qty_cols = [c for c in cleaned_df.columns if "quanity" in c or c == "qty"]

    #Convert these columns to numeric, turning invalid values into NaN
    for col in price_cols + qty_cols: 
        cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors="coerce")

    #Drop rows where any critical numbers column is missing
    critical_cols = price_cols + qty_cols
    if critical_cols: 
        cleaned_df = cleaned_df.dropna(subset=critical_cols)

    return cleaned_df

#Function is to remove invalid rows with negative prices or quantities.
#Negative values are treated as data entry errors and removed. 
def remove_invalid_rows(df):
    """Remove rows with negative prices or quantities."""

    cleaned_df = df.copy()

    #Find price and quantity columns 
    price_cols = [c for c in cleaned_df.columns if "price" in c]
    qty_cols = [c for c in cleaned_df.columns if "quantity" in c or c == "qty"]

    #Keep only rows with non-negative prices
    for col in price_cols:
        cleaned_df = cleaned_df[cleaned_df[col] >= 0]

    #Keep only rows with non-negative quantities
    for col in qty_cols:
        cleaned_df = cleaned_df[cleaned_df[col] >= 0]

    return cleaned_df

#Run the full cleaning pipeline when the script is executed directly.
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    #Make sure the processed folder exists
    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)

    #Load raw data and apply cleaning steps 
    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    #Save the cleaned data
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())

    #Note: Github Copilot was enabled and attempted during this assignment by writing descriptive comments to prompt code suggestions. 
