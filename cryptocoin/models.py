from django.db import models

# Create your models here.


class Coins(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    volume = models.DecimalField(decimal_places=2, max_digits=30)
    twenty_four_hour_percentage = models.DecimalField(decimal_places=2, max_digits=10)
    seven_day_percentage = models.DecimalField(decimal_places=2, max_digits=10)
