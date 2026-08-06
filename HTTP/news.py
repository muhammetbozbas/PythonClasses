import requests

headlines_url = "https://newsapi.org/v2/top-headlines"
everything_url = "https://newsapi.org/v2/everything"

api_key = "d14e97eaf1f54578acadd25850fedd38"

# response = requests.get(headlines_url, params= {
#     "apiKey" : api_key,
#     "country" : "us"
# })

response = requests.get(everything_url, params= {
    "apiKey" : api_key,
    "q" : "salah",
    "language": "en",
    "sortby" : "publishedAt"
})

news = response.json()["articles"]

for i in news:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])
    # print(i["content"])
