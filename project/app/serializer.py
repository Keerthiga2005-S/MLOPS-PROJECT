from rest_framework import serializers
from .models import InputData

class InputDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputData
        fields = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure', 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']