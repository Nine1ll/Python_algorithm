from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MJU_ID = "Your MJU ID"
MJU_PASSWORD = "Your MJU PassWord"
# TODO 1: 내 강의실 있는 li 먼저 sort 해서 "과제 등록 현황"일 때 크롤링 해야함
# TODO 2: "과제 등록 현황"에서는 과제 제출 마감시간을 알 수 없는 문제 발생


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
        command = input("번호를 선택하세요.\n1. 모든 과제 불러오기 \n2. 과목별 불러오기\n3. 요일별 불러오기.\n4. 달력 형태로 불러오기\n 숫자를 입력하세요.: ")

        if command == "1":
            driver.find_element('xpath', '//*[@id="MENU"]/li[1]/a').click()
            request = driver.page_source
            soup = BeautifulSoup(request, 'html.parser')
            subjects_html = soup.find("table", class_='list UItable')
            print(subjects_html.text)
            # 'tr' tr의 2번째 td가 과목명, 4번째 td안에
            # span class_="button small"안에 a에 과목으로 넘어가는 a있음
        elif command == "2":
            """과목별 불러오기"""
            subject_name = input("과목명을 입력하세요. (종료를 원할시 exit 입력) : ")
            pass
        elif command == "3":
            """요일별 불러오기"""
            day = input("요일을 입력하세요.: ")
            # swtich문 사용 필요.
            pass
        else:
            print("모든 과목을 달력 형태로 불러옵니다.")
        # request = driver.page_source
        #
        # soup = BeautifulSoup(request, 'html.parser')
        # homeworks_html = soup.find("ul", class_='eClassList')
        # # print(type(homeworks_html)) # <class 'bs4.element.Tag'>
        # homeworks = homeworks_html.find_all('li')
        # print(homeworks_html)
        # # for homework in homeworks:
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
