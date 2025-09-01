from bs4 import BeautifulSoup
import requests

URL="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
emp_webpage = response.text
soup = BeautifulSoup(emp_webpage, "html.parser")

movie_name = soup.find_all(name="h3", class_="title")

with open("movies.txt","w") as file:
    for i in range(len(movie_name)-1,-1,-1):
        file.write(f"{movie_name[i].get_text()}\n")
