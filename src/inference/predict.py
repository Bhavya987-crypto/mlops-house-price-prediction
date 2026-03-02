import logging


class ModelInference:
    def predict(self, model, input_data):
        logging.info("Running inference...")
        prediction = model.predict(input_data)
        logging.info("Inference completed.")
        return prediction
