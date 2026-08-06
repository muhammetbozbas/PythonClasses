import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts", data= {
    "title": "et porro",
    "body": "tempora",
    "userId": 1
})

result = response   #<Response [201]> ==> succesfull
result = response.text
result = response.json()
result = response.headers

print(result)