from django.contrib import admin
from .models import Coins

# Register your models here.


class Coin_Data_Admin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "volume",
        "twenty_four_hour_percentage",
        "seven_day_percentage",
    ]


admin.site.register(Coins, Coin_Data_Admin)
