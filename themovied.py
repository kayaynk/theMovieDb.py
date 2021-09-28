

import requests


class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "c5986ae147442eee5a3ff8f8397a2da8"

    def getPopulars(self):
        responce = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return responce.json()
    def getSearch(self,keyw):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyw}&language=en-US&page=1")
        return  response.json()
movieApi = theMovieDb()
while True:
    select = input("1- Popular Movies\n2- Search Movies\n3- Exit\nSelect Action: ")

    if select == "3":
        break
    else:
        if select == "1":
            result = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie["title"])
        elif select =="2":
            keyw = input("keyword: ")
            movies = movieApi.getSearch(keyw)
            for movie in movies["results"]:
                print(movie["name"])

        else:
            print("Incorrect Entry")
