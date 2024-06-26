import pandas as pd

class Helpers:
    @staticmethod
    def read_csv_file(file_path, delimiter=','):
        """
        Reads a CSV file into a DataFrame.

        Parameters:
        - file_path (str): Path to the CSV file.
        - delimiter (str): Delimiter used in the CSV file. Default is ','.

        Returns:
        - DataFrame: DataFrame containing the data from the CSV file.
        """
        return pd.read_csv(file_path, delimiter=delimiter)

    @staticmethod
    def write_csv_file(df, file_path, index=False):
        """
        Writes a DataFrame to a CSV file.

        Parameters:
        - df (DataFrame): DataFrame to be saved.
        - file_path (str): Path to save the CSV file.
        - index (bool): Whether to include the index in the CSV file. Default is False.
        """
        df.to_csv(file_path, index=index)
        
    def read_config(file_path):
        """
        Read configuration from a YAML file into a dictionary.

        Parameters:
        - file_path: Path to the YAML file containing the configuration.

        Returns:
        - Dictionary containing the loaded configuration data.
        """
        with open(file_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    def feature_engineering(df, columns, types):
        """
        Performs feature engineering by casting specified columns to specified data types.

        Parameters:
        - df (DataFrame): DataFrame containing the data.
        - columns (list): List of column names to be cast.
        - types (list): List of data types corresponding to the columns.

        Returns:
        - DataFrame: DataFrame with specified columns cast to specified data types.
        """
        if len(columns) != len(types):
            raise ValueError("Length of 'columns' and 'types' lists must be the same.")

        for column, new_type in zip(columns, types):
            df[column] = df[column].astype(new_type)
        
        return df
