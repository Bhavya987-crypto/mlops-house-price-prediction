import pandas as pd
import logging


class DataPreprocessing:
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Starting data preprocessing...")

        df = df.dropna()

        logging.info("Data preprocessing completed.")
        return df
