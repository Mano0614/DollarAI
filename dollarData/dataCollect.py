from urllib.parse import quote_plus 
from bs4 import BeautifulSoup as bs   

from selenium import webdriver
import time
from urllib.request import (urlopen, urlparse, urlunparse, urlretrieve)

chrome_path ='C:\\Users\\최재영\\Downloads\\chromedriver_win32\\chromedriver.exe'
base_url = "https://www.google.co.kr/imghp"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("lang=ko_KR") # 한국어
chrome_options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(chrome_path,chrome_options=chrome_options)
driver.get(base_url)
driver.implicitly_wait(3)
driver.get_screenshot_as_file('google_screen.png')
driver.close()

def selenium_scroll_option():
    SCROLL_PAUSE_SEC = 3
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_SEC)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break
        last_height = new_height
    
    
five_dollar = './5 dollar/'
ten_dollar = './10 dollar/'
twenty_dollar = './20 dollar/'
fifty_dollar = './50 dollar/'
hunread_dollar ='./100 dollar/'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import urllib.request
import os
import pandas as pd

# 키워드 검색하기

a=input("검색할 키워드를 입력 : ")
image_name = input("저장할 이미지 이름 : ")
driver = webdriver.Chrome(chrome_path)
driver.get('http://www.google.co.kr/imghp?hl=ko')
browser = driver.find_element(By.NAME, "name")
browser.send_keys("ChromeDriver")
browser.send_keys(Keys.RETURN)




selenium_scroll_option() 
driver.find_elements_by_xpath('//*[@id="islmp"]/div/div/div/div/div[3]/div[2]/input')[0].click() # 이미지 더보기 클릭
selenium_scroll_option()



'''이미지 src요소를 리스트업해서 이미지 url 저장'''

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #  클래스 네임에서 공백은 .을 찍어줌
images_url = []
for i in images: 

    if i.get_attribute('src')!= None :
        images_url.append(i.get_attribute('src'))
    else :
        images_url.append(i.get_attribute('data-src'))
driver.close()



# 겹치는 이미지 url 제거

print("전체 다운로드한 이미지 개수: {}\n동일한 이미지를 제거한 이미지 개수: {}".format(len(images_url), len(pd.DataFrame(images_url)[0].unique())))
images_url=pd.DataFrame(images_url)[0].unique()

if image_name == "5 dollar":
    for t, url in enumerate(images_url, 0):
        urlretrieve(url, five_dollar + image_name + "_" + str(t) + ".jpg")
    driver.close()

elif image_name == "10 dollar":
    for t, url in enumerate(images_url, 0):
        urlretrieve(url, ten_dollar + image_name + "_" + str(t) + ".jpg")
    driver.close()

if image_name == "20 dollar":
    for t, url in enumerate(images_url, 0):
        urlretrieve(url, twenty_dollar + image_name + "_" + str(t) + ".jpg")
    driver.close()
    

if image_name == "50 dollar":
    for t, url in enumerate(images_url, 0):
        urlretrieve(url, fifty_dollar + image_name + "_" + str(t) + ".jpg")
    driver.close()
    

if image_name == "100 dollar":
    for t, url in enumerate(images_url, 0):
        urlretrieve(url, hunread_dollar + image_name + "_" + str(t) + ".jpg")
    driver.close()