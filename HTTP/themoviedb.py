import requests

class TheMovie:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "529f3a96627c7eabf5ec6f34eba95002"

    def search(self,data):
        response = requests.get(self.api_url + "search/movie", params={
            "api_key": self.api_key,
            "query": data,
        })
        return response.json()
    
    def popular(self):
        response = requests.get(self.api_url + "movie/popular", params= {
            "api_key": self.api_key,
            "page": "1"
        })
        return response.json()

    def now_playing(self):
        response = requests.get(self.api_url + "movie/now_playing", params= {
            "api_key": self.api_key,
            "page": "1"
        })
        return response.json()
    
movie = TheMovie()
while True:
    choice = input("1- Search\n2- Tops\n3- In the vision\n4- Exit\nYour Choice: ")
    if choice == "4":
        break
    else:
        if choice == "1":
            data = input("Name: ")
            for m in movie.search(data)["results"]:
                print(m["title"])
        elif choice == "2":
            for m in movie.popular()["results"]:
                print(m["title"])
        elif choice == "3":
            for m in movie.now_playing()["results"]:
                print(m["title"])
        else:
            print("Wrong Choice")