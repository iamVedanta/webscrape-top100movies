from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies = response.text

soup = BeautifulSoup(movies, "html.parser")

titles = soup.find_all(name="h3", class_="title")
titles_list = []
for title in titles:
    titles_list.append(title.getText())

print(titles_list)
arranged_movies = list(reversed(titles_list))

f = open("movies.txt",'a', encoding="utf-8")
for movie in arranged_movies:
    f.write(f"{movie}\n")
f.close()
