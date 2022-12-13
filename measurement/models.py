from django.db import models
import PIL
# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    discription = models.CharField(max_length=50)


class Measurment(models.Model):
    temperature = models.FloatField()
    date = models.DateField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensors')
    pic = models.ImageField(max_length=100, upload_to='pics/', null=True)
