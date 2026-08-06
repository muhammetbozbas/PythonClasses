import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

result = response
result = type(response)
result = response.status_code
result = response.headers
result = response.headers["Content-Type"]
result = response.url
result = response.encoding
result = response.text
todos = json.loads(response.text)
result = todos[2]["title"]

for i in todos:
    if i["userId"] == 1:
        print(i["title"])


print(result)