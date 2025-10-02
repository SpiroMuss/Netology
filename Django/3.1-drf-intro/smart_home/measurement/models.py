from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название датчика')
    description = models.CharField(max_length=100, blank=True, verbose_name='Название датчика')

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(verbose_name='Температура', decimal_places=1, max_digits=3)
    created_at = models.DateTimeField(verbose_name='Дата и время', auto_now_add=True)