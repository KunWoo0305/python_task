import gmaps as gmaps
import googlemaps as googlemaps
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import time
import folium
import googlemaps

url = "https://banapresso.com/store"

driver = webdriver.Chrome(executable_path='/Users/eung/Desktop/python/pythonProject1/driver/chromedriver')
driver.get(url)
request = requests.get(url)

# page1
html = driver.page_source
soup = BeautifulSoup(html)

# store list
store_area = soup.findAll('span', {'span', 'store_name_map'})

#데이터 배열 만들기
store_info = []

# 데이터 가져오기
for i in range(len(store_area)):
    store_info.append([store_area[i].find('i').text, store_area[i].find('span').text])

# page2, 5
# 다음페이지로 이동
# xpath : //*[@id="contents"]/article/div/section[1]/div/div[1]/div[3]/span/a


for i in range(2, 6):
    driver.find_element('xpath', '//*[@id="contents"]/article/div/section[1]/div/div[1]/div[3]/ul/li['+ str(i)+']/a').click()
    # 딜레이 주기
    time.sleep(0.5)

    html = driver.page_source
    soup = BeautifulSoup(html)

    # store list
    store_area = soup.findAll('span', {'span', 'store_name_map'})

    # 데이터 가져오기
    for i in range(len(store_area)):
        store_info.append([store_area[i].find('i').text, store_area[i].find('span').text])

# page6
driver.find_element('xpath', '//*[@id="contents"]/article/div/section[1]/div/div[1]/div[3]/span/a').click()
# 딜레이 주기
time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html)

# store list
store_area = soup.findAll('span', {'span', 'store_name_map'})

# 데이터 가져오기
for i in range(len(store_area)):
    store_info.append([store_area[i].find('i').text, store_area[i].find('span').text])

for i in range(2, 5):
    driver.find_element('xpath', '//*[@id="contents"]/article/div/section[1]/div/div[1]/div[3]/ul/li['+ str(i)+']/a').click()
    # 딜레이 주기
    time.sleep(0.5)

    html = driver.page_source
    soup = BeautifulSoup(html)

    # store list
    store_area = soup.findAll('span', {'span', 'store_name_map'})

    # 데이터 가져오기
    for i in range(len(store_area)):
        store_info.append([store_area[i].find('i').text, store_area[i].find('span').text])

# 85
print(store_info)
location = []

for i in range(len(store_info)):
    store_address = store_info[i][1]
    store_name = store_info[i][0]

    gmaps = googlemaps.Client(GOOGLE_API_KEY)
    geocode_result = gmaps.geocode(store_address, language='ko') # 한국어 설정으로 인천대공원의 결과값을 받아온다.

    cafe_lat = geocode_result[0]["geometry"]["location"]["lat"] # 리스트에서 위도 추출
    cafe_log = geocode_result[0]["geometry"]["location"]["lng"] # 리스트에서 경도 추출

    popup = folium.Popup(store_name, max_width=500)
    folium.Marker(location=[cafe_lat, cafe_log], popup=popup).add_to(cafe_map)

    cafe_map.save('./cafe_map.html')

cafe_map

