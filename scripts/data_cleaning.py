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