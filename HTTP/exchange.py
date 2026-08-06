import requests

api_key = "9f21854234e5ce850a9acd61"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz türü: ")
alinan_doviz = input("Alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozmak istiyorsunuz: "))

exchange = requests.get(api_url + bozulan_doviz)
result = exchange.json()["conversion_rates"][alinan_doviz]

print(result * miktar)