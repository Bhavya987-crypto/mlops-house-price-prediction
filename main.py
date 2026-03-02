import logging
from src.utils.common import setup_logging
from src.data_ingestion.data_ingestion import DataIngestion
from src.preprocessing.preprocessing import DataPreprocessing
from src.training.train import ModelTrainer


def run_pipeline(data_path: str, target_column: str):
    setup_logging()

    logging.info("Pipeline started.")

    # Data Ingestion
    ingestion = DataIngestion(data_path)
    df = ingestion.load_data()

    # Preprocessing
    preprocessing = DataPreprocessing()
    df_clean = preprocessing.clean_data(df)

    # Training
    trainer = ModelTrainer()
    model, mse = trainer.train(df_clean, target_column)

    logging.info(f"Pipeline completed successfully. Final MSE: {mse}")

    return model


if __name__ == "__main__":
    model = run_pipeline("data/housing.csv", "price")
