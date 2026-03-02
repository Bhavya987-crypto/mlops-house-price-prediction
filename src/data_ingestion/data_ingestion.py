import pandas as pd
import logging
import os


class DataIngestion:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_data(self) -> pd.DataFrame:
        logging.info("Loading dataset...")
        df = pd.read_csv(self.data_path)
        logging.info("Dataset loaded successfully.")
        return df
