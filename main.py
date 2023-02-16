import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

URL = "https://fayni-recepty.com.ua/recepty/pershi-stravy/"

print(URL)
while True:
  site_page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(site_page.content, "html.parser")

  first_dishes = soup.find_all("h2", class_="entry-title")
  for dish in first_dishes:
    dish_name = dish.a.text
    print(dish_name)

  next_page = soup.select_one('a.next')

  if next_page:
    next_url = next_page.get('href')
    URL = urljoin(URL, next_url)
  else:
    break



