import requests
from bs4 import BeautifulSoup
def parse_ukd_data():
    url = 'https://ukd.edu.ua/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(class_= 'col-lg-9 col-md-12')
    dropdown = results.find('ul')
    speciality = dropdown.find_all('li')

    for element in speciality:
        speciality_name = element.text.strip()
        print(speciality_name)

parse_ukd_data()
