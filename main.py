import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}
# define a base URL

URL = "https://www.work.ua/jobs/?page=1"

print(URL)
#while True:
site_page = requests.get(URL, headers=headers)
print(site_page.status_code)

soup = BeautifulSoup(site_page.content, "html.parser")

jobs = soup.find_all('div', class_ = 'card card-hover card-visited wordwrap job-link js-hot-block')
file = open("output.txt", "w")

output_str = ""
for row in jobs:
    output_str += str(row) + "\n"

file = open("output.html", "w")
file.write(output_str)
file.close()
