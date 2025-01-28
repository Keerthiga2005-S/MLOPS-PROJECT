from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from sklearn.linear_model import LogisticRegression
from .models import InputData

class PredictView(APIView):
    def get(self, request):
        return Response({'message': 'All ok'}, status=status.HTTP_200_OK)

    def post(self, request):
        # Get input values from the request data
        age = int(request.data.get('age'))
        anaemia = int(request.data.get('anaemia'))
        creatinine_phosphokinase = int(request.data.get('creatinine_phosphokinase'))
        diabetes = int(request.data.get('diabetes'))
        ejection_fraction = float(request.data.get('ejection_fraction'))
        high_blood_pressure = int(request.data.get('high_blood_pressure'))
        serum_creatinine = float(request.data.get('serum_creatinine'))
        serum_sodium = int(request.data.get('serum_sodium'))
        sex = int(request.data.get('sex'))
        smoking = int(request.data.get('smoking'))
        time = int(request.data.get('time'))

        # Check if any input value is missing
        if None in [age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, serum_creatinine, serum_sodium, sex, smoking, time]:
            return Response({'error': 'One or more input values are missing'}, status=status.HTTP_400_BAD_REQUEST)

        # Read the dataset
        data = pd.read_csv('C:\\Users\\skeer\\OneDrive\\Desktop\\react-django\\project\\project\\heart_failure_clinical_records_dataset.csv')  # Provide the correct path to your dataset

        # Prepare input features and target variable
        x = data[['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure', 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']]
        y = data['DEATH_EVENT']  

        # Train a logistic regression model
        logistic_reg = LogisticRegression()
        logistic_reg.fit(x, y)

        # Predict the output based on input values
        input_data = [[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, serum_creatinine, serum_sodium, sex, smoking, time]]
        prediction = logistic_reg.predict(input_data)
        predicted_probability = logistic_reg.predict_proba(input_data)[0][1]

        # Process the output
        if prediction[0] == 1:
            output_formatted = 'DEATH_EVENT: Highly Possible'
        else:
            output_formatted = 'DEATH_EVENT: Low Possible'

        return Response({'output': output_formatted, 'predicted_probability': predicted_probability}, status=status.HTTP_200_OK)
