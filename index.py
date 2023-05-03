import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
movies_table = soup.find('table', {'class': 'chart full-width'})
movies = movies_table.select('tbody.lister-list tr')

with open('top_movies.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Year'])

    for movie in movies:
        title = movie.find('td', class_='titleColumn').find('a').get_text()
        year = movie.find('span', class_='secondaryInfo').get_text()[1:5]
        writer.writerow([title, year])

print('Top movies saved to top_movies.csv')
