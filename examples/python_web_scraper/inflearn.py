import requests
from bs4 import BeautifulSoup

LIMIT = 1
URL = f"https://www.inflearn.com/courses/it-programming?order=seq&page={LIMIT}"


def extract_inflearn_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination_container"})
    links = pagination.find_all("li")

    pages = []
    for link in links:
        pages.append(link.find("a").string)
        max_page = int(pages[-1])
    return max_page


def extract_inflearn_lectures(last_page):
    lectures = []
    for page in range(last_page):
        result = requests.get(f"{URL}{page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find(
            "div", {"class": "columns is-multiline is-mobile courses_card_list_body"})
        title = results.find("p").string
        print(title)
        lectures.append(title)
    return(lectures)
