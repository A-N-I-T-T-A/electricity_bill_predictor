from django.db import models

# Create your models here.
import pandas as pd

class BillPredictor:
    def __init__(self, dataset_path):
        self.dataset = pd.read_csv(dataset_path)
        self.dataset = self.dataset.sort_values(by='Units_Consumed')

    def predict_bill(self, units):
        closest_row = self.dataset.iloc[(self.dataset['Units_Consumed'] - units).abs().argsort()[:1]]
        
        return float(closest_row['Electricity_Bill'].values[0])