import requests
from bs4 import BeautifulSoup

LIMIT=1
URL= f"https://www.inflearn.com/courses/it-programming?order=seq&page={LIMIT}"

def extract_inflearn_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination_container"})
    links = pagination.find_all("li")

    pages=[]
    for link in links:
        pages.append(link.find("a").string)
        max_page=int(pages[-1])
    return max_page

def extract_inflearn_lectures(last_page):
    lectures=[]
    for page in range(last_page):
        result=requests.get(f"{URL}{page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find("div", {"class": "columns is-multiline is-mobile courses_card_list_body"})
        titles = results.find("p").string
        print(titles)
    
    return(lectures)


# 느낀점:
# 내가 자주 이용하는 인프런의 무료강의,유료강의 분리하고, 파이썬,go,등등 다양하게 스크래핑하고 싶어서
# 10개 이상이 넘어가면 똑같은 자료가 반복되는 문제 때문에 하루종일 시간을 보냈는데..
# 보안이 되어 있다는 걸 뒤늦게 알고 좌절. ㅠㅠ 이렇게도 가능하다라는 것만 보면 됐을껄.
# 아무튼 간단한 코드로 이렇게 내가 원하는 데이터를 추출할 수 있다는 걸 알려준 과제.