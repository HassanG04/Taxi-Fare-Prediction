from django.test import TestCase
from django.urls import reverse

class PredictionTest(TestCase):
    def test_prediction_form(self):
        response = self.client.post(reverse('predict_fare'), {
            'Car Condition': 'Good',
            'Weather': 'Clear',
            'Traffic Condition': 'Light',
            'pickup_datetime': '2025-08-09 10:00:00',
            'pickup_longitude': -73.985428,
            'pickup_latitude': 40.748817,
            'dropoff_longitude': -73.985130,
            'dropoff_latitude': 40.758896,
            'passenger_count': 2,
            'hour': 10,
            'day': 9,
            'month': 8,
            'weekday': 6,  # Saturday
            'year': 2025,
            'jfk_dist': 20.5,
            'ewr_dist': 18.2,
            'lga_dist': 15.4,
            'sol_dist': 5.1,
            'nyc_dist': 2.3,
            'distance': 3.5,
            'bearing': 45.0,
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Predicted Fare')
