from django.shortcuts import render
from .models import BillPredictor
import os

# Load the dataset when the server starts
dataset_path = os.path.join(os.path.dirname(__file__), '../electricity_bill.csv')
predictor = BillPredictor(dataset_path)

def predict_view(request):
    bill_amount = None
    if request.method == 'POST':
        units = float(request.POST['units'])
        bill_amount = predictor.predict_bill(units)  # Use trained model for prediction
    return render(request, 'index.html', {'bill_amount': bill_amount})
