from bs4 import BeautifulSoup
from requests import get
# 학교 홈페이지는 req

def extract_task():

    base_url = 'https://home.mju.ac.kr/mainIndex/myHomeworkList.action?command=&tab=homework'
    request = get(base_url, headers={"User-Agent": "Nine1ll"})
    print(request.text)


extract_task()