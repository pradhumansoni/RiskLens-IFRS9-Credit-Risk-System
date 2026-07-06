import pandas as pd
import os

def load_data(filepath="data/merged_dataset.csv"):
    """
    Loads the primary merged dataset from a specified filepath.

    Args:
        filepath (str): The relative path to the dataset. Defaults to "data/merged_dataset.csv".

    Returns:
        pd.DataFrame: The loaded DataFrame if successful, None otherwise.
    """
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found. Please ensure the path is correct.")
        return None
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded data from '{filepath}'.")
        print(f"DataFrame shape: {df.shape}")
        print("\nDataFrame Info:")
        df.info()
        return df
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None
