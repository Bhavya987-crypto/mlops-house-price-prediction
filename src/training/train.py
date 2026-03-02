import logging
import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


class ModelTrainer:
    def train(self, df, target_column: str):
        logging.info("Starting model training...")

        X = df.drop(columns=[target_column])
        y = df[target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LinearRegression()
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)

        os.makedirs("artifacts", exist_ok=True)
        joblib.dump(model, "artifacts/model.pkl")

        logging.info(f"Model training completed. MSE: {mse}")
        logging.info("Model saved to artifacts/model.pkl")

        return model, mse
