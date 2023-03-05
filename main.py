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

# write jobs variable content to a html file
output_str = ""
for row in jobs:
    output_str += str(row) + "\n"

file = open("output.html", "w")
file.write(output_str)
file.close()

# find a job title name
#for job in jobs:
job_title_class = soup.find_all('div', class_ = "card card-hover card-visited wordwrap job-link js-hot-block")
for job_title in job_title_class:
  job_title_name = job_title.find_all('h2')
  for h2_tag in job_title_name:
     job_name = h2_tag.text
    
with open('work_ua.csv', "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(str(job_title_name))
