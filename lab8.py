import requests
from bs4 import BeautifulSoup


def parse_ukd_data():
    url = 'https://ukd.edu.ua/'
    page = requests.get(url)  # отримання запиту GET зі змінної URL-адреси
    soup = BeautifulSoup(page.content, "html.parser")  # отримання вмісту сторінки та специфікатора аналізатора

    class_with_tags = soup.find("div", class_='col-lg-9 col-md-12')  # пошук класу з тегами професій
    ul_tag = class_with_tags.find('ul')  # знайти тег 'ul'
    prof_names = ul_tag.find_all('li')  # у тегу ul знайдіть тег 'li', де розміщені назви професій

    prof_list = []
    for element in prof_names:
        speciality_name = element.text.strip()  # взяти весь рядок з тегу та додати до списку
        prof_list.append(speciality_name)
    print("Список професій:")
    print()
    for item in prof_list:  # роздрукувати список професій
        print(item)

    return prof_list


parse_ukd_data()
