from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MJU_ID = "YOUR MJU ID"
MJU_PASSWORD = "YOUR MJU PASSWORD"


def homework_manage():
    """ e-class 페이지에 아이디와 비밀번호 입력 후 접속,
    과제 제출, 마감 기한을 알려주는 method """

    driver = webdriver.Chrome('chromedriver')
    url = 'https://home.mju.ac.kr/user/index.action'
    driver.get(url)
    time.sleep(2)
    driver.find_element("xpath", '//*[@id="classlogin"]/div/div[2]/div[1]/div[2]/a[1]').click()
    time.sleep(3)
    try:
        driver.find_element('name', 'id').send_keys(MJU_ID)
        driver.find_element('name', 'passwrd').send_keys(MJU_PASSWORD)
        time.sleep(2)
        driver.find_element('xpath', '//*[@id="loginButton"]').click()
        request = driver.page_source

        soup = BeautifulSoup(request, 'html.parser')
        homeworks_html = soup.find("ul", class_='eClassList')
        # print(type(homeworks_html)) # <class 'bs4.element.Tag'>
        homeworks = homeworks_html.find_all('li')
        print(homeworks_html)
        # for homework in homeworks:
        #     try:
        #         subject_name = homework.find('strong').string.strip()
        #     except AttributeError:
        #         subject_name = None
        #     print(subject_name)
        #
        #     submit_list = homework.find('dd', class_="information")
        #     submits = submit_list.find_all("p", class_='gab')
        #     # AttributeError 만들어짐 -> 아래 'ul', class_='paging 해결 필요
        #     for submit in submits:
        #         print(submit.string)

    except:
        print("아이디, 비밀번호를 확인 하세요.")

    driver.quit()


homework_manage()
