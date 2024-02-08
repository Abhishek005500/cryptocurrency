import requests
from django.shortcuts import render


user_input = str(input("what cryptocurrenccy would you like information for?"))
response = requests.get("https://api.coincap.io/v2/assets/" + user_input.lower())
# print(response.json())
data = response.json()
print(data["data"].get("name"))
if response.status_code != 200:
    print("Error trying to retrive data.")
else:
    print("crptocurrency :", response.json()["data"]["name"])
    print("priceUSD :", response.json()["data"]["priceUsd"])
    print("Market Cap (USD) :", response.json()["data"]["marketCapUsd"])
    print("Change percent 24hr :", response.json()["data"]["changePercent24Hr"])
    # print("Change percent 7hr :", response.json()["data"]["changePercent7Hr"])
