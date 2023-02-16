import requests
import csv
import openpyxl
from bs4 import BeautifulSoup
from urllib.parse import urljoin


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

URL = "https://fayni-recepty.com.ua/recepty/pershi-stravy/"
first_dishes_name = []
print(URL)

# Going throw all pages

while True:
  site_page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(site_page.content, "html.parser")

  first_dishes = soup.find_all("h2", class_="entry-title")
  for dish in first_dishes:
    dish_name = dish.a.text
    first_dishes_name.append(dish_name)

  next_page = soup.select_one('a.next')

  if next_page:
    next_url = next_page.get('href')
    URL = urljoin(URL, next_url)
  else:
    break

# Create and write results into .csv file

with open('pershi-stravy.csv', 'w', newline='') as csv_file:
  csv_writer = csv.writer(csv_file)
  csv_writer.writerow(['name'])

# Create and write results into .xlsx file

excel_file = openpyxl.Workbook()
excel_writer = excel_file.active
excel_writer['A1'] = 'name'

for first_dish in first_dishes_name:
  excel_writer.append([first_dish])

excel_file.save('ershi-stravy.xlsx')

