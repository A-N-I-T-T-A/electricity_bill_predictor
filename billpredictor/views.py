from django.shortcuts import render
from .models import BillPredictor
import os

predictor = BillPredictor(os.path.join(os.path.dirname(__file__), '../electricity_bill.csv'))

def predict_view(request):
    bill_amount = None
    if request.method == 'POST':
        units = float(request.POST['units'])
        bill_amount = predictor.predict_bill(units)
    return render(request, 'index.html', {'bill_amount': bill_amount})