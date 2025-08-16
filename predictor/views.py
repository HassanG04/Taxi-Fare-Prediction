from django.shortcuts import render
import pandas as pd
import joblib
import os

# Load model once
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(MODEL_PATH)

def predict_fare(request):
    if request.method == 'POST':
        # Extract all features from the form
        data = {
            'Car Condition': [request.POST.get('Car Condition')],
            'Weather': [request.POST.get('Weather')],
            'Traffic Condition': [request.POST.get('Traffic Condition')],
            'pickup_datetime': [request.POST.get('pickup_datetime')],
            'pickup_longitude': [float(request.POST.get('pickup_longitude'))],
            'pickup_latitude': [float(request.POST.get('pickup_latitude'))],
            'dropoff_longitude': [float(request.POST.get('dropoff_longitude'))],
            'dropoff_latitude': [float(request.POST.get('dropoff_latitude'))],
            'passenger_count': [int(request.POST.get('passenger_count'))],
            'hour': [int(request.POST.get('hour'))],
            'day': [int(request.POST.get('day'))],
            'month': [int(request.POST.get('month'))],
            'weekday': [int(request.POST.get('weekday'))],
            'year': [int(request.POST.get('year'))],
            'jfk_dist': [float(request.POST.get('jfk_dist'))],
            'ewr_dist': [float(request.POST.get('ewr_dist'))],
            'lga_dist': [float(request.POST.get('lga_dist'))],
            'sol_dist': [float(request.POST.get('sol_dist'))],
            'nyc_dist': [float(request.POST.get('nyc_dist'))],
            'distance': [float(request.POST.get('distance'))],
            'bearing': [float(request.POST.get('bearing'))]
        }

        df = pd.DataFrame(data)
        fare = model.predict(df)[0]

        return render(request, 'result.html', {'fare': fare})

    # If GET request → show form
    return render(request, 'predict_form.html')
