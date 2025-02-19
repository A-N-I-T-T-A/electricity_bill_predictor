import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class BillPredictor:
    def __init__(self, dataset_path):
        self.dataset = pd.read_csv(dataset_path)
        self.model = LinearRegression()

        # Prepare the data
        X = self.dataset['Units_Consumed'].values.reshape(-1, 1)
        y = self.dataset['Electricity_Bill'].values        # Dependent variable

        # Train the model
        self.model.fit(X, y)

    def predict_bill(self, units):
        units_array = np.array([[units]])  # Convert to 2D array for prediction
        prediction = self.model.predict(units_array)
        return float(prediction[0])  # Convert to float for easy display
