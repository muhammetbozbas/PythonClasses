import requests

class GitHub:
    def __init__(self):
        self.api_url = "https://api.github.com"


    def getUser(self,username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()
    
    def getRepositories(self,username):
        response = requests.get(self.api_url + "/users/" + username + "/repos")
        return response.json()
    
github = GitHub()

while True:
    print("*********".center(50,'*'))
    choice = input("1- Find User\n2- Get Repositories\n3- Exit\nYour Choice: ")

    if choice == '3':
        break
    else:
        if choice == "1":
            username = input("Username: ")
            result = github.getUser(username)
            print(f"Name: {result["name"]}, Number of repos: {result["public_repos"]}, Followers: {result["followers"]}")

        elif choice == "2":
            username = input("Username: ")
            result = github.getRepositories(username)
            for r in result:
                print(r['name'])
        else:
            print("Wrong Choice")

