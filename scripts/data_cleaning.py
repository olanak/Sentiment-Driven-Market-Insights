import pandas as pd

def standardize_columns(datasets):
    """
    Standardizes the column names by making them lowercase and replacing spaces with underscores.
    :param datasets: Dictionary of DataFrames.
    :return: Dictionary of cleaned DataFrames.
    """
    for name, df in datasets.items():
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return datasets

def handle_missing_values(datasets):
    """
    Handles missing values by filling them with 0.
    :param datasets: Dictionary of DataFrames.
    :return: Dictionary of cleaned DataFrames.
    """
    for name, df in datasets.items():
        df.fillna(0, inplace=True)
    return datasets

def convert_dates(datasets):
    """
    Converts date columns to datetime format.
    :param datasets: Dictionary of DataFrames.
    :return: Dictionary of DataFrames with date columns converted.
    """
    for name, df in datasets.items():
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return datasets

def merge_data(file_paths):
    # Load and merge all stock dataframes into one
     stock_dataframes = []
     for file in file_paths:
         ticker = file.split('/')[-1].split('_')[0]  # Extract ticker from file name
         df = pd.read_csv(file)
         df['Ticker'] = ticker  # Add ticker column
         stock_dataframes.append(df)

         merged_stock_df = pd.concat(stock_dataframes, ignore_index=True)
         merged_stock_df.to_csv('../data/processed/merged_stock_data.csv', index=False)
        
     return merged_stock_df