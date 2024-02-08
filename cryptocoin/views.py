from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from django.shortcuts import render
import requests


def home(request):
    if request.method == "POST":
        input1 = request.POST.get("name").lower()
        print(input1)
        response = requests.get(f"https://api.coincap.io/v2/assets/{input1}/")
        data = response.json()
        print(data)
        if response.status_code != 200:
            print("Error trying to retrive data.")
        else:
            fetch_data = {
                "name": data["data"].get("name"),
                "price": round(float(data["data"].get("priceUsd")), 2),
                "volume": round(float(data["data"].get("marketCapUsd")), 2),
                "24_hr_change": round(float(data["data"].get("changePercent24Hr")), 2),
            }

            print(fetch_data)
            return render(request, "show.html", {"data": fetch_data})

    else:
        return render(request, "show.html")
