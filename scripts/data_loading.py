import pandas as pd

def load_historical_datasets(file_paths):
    """ Loads historical datasets from provided file paths
    and returns a dictionary of DataFrames.

    Args:
        file_paths (str): List of paths to CSV files containing stock data.

    Returns:
        Dictionary of DataFrames indexed by filename.
    """
    datasets = {}
    for file_path in file_paths:
        datasets[file_path] = pd.read_csv(file_path)
    return datasets


def load_raw_analyst_ratings(file_path):
    """
    Load stock data from a csv file

    Args:
        file_path (str): path to the csv file

    Returns:
        pd.DataFrame: loaded data
    """
    return pd.read_csv(file_path)