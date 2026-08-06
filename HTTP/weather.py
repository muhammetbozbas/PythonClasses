import requests

url = "http://api.weatherapi.com/v1/current.json"
access_key = "71a5a96a570f468091e201957260508"

region_user = input("Region: ")

forecast = requests.get(url, params={
    'key' : access_key,
    'q' : region_user,
    'lang':  "tr"
})
result = forecast.json()
region = result["location"]["name"]
temp = result["current"]["temp_c"]
text = result["current"]["condition"]["text"]

print(f"The weather is {temp} degrees and {text.lower()} in {region} right now.")