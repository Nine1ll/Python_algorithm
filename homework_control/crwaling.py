from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MJU_ID = "ENTER YOUR ID"
MJU_PASSWORD = "ENTER YOUR PASSWORD"


def path_to_go():
    driver = webdriver.Chrome('chromedriver')
    url = 'https://home.mju.ac.kr/user/index.action'
    driver.get(url)

    driver.find_element("xpath", '//*[@id="classlogin"]/div/div[2]/div[1]/div[2]/a[1]').click()
    time.sleep(5)

    driver.find_element('name', 'id').send_keys("")
    driver.find_element('name', 'passwrd').send_keys("")

    driver.find_element('xpath', '//*[@id="loginButton"]').click()

    driver.find_element('class', 'eClassList')

path_to_go()