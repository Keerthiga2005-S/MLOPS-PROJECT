from django.db import models

class InputData(models.Model):
    age = models.IntegerField()
    anaemia = models.BooleanField()
    creatinine_phosphokinase = models.IntegerField()
    diabetes = models.BooleanField()
    ejection_fraction = models.FloatField()
    high_blood_pressure = models.BooleanField()
    serum_creatinine = models.FloatField()
    serum_sodium = models.IntegerField()
    sex = models.BooleanField()
    smoking = models.BooleanField()
    time=models.IntegerField()
