from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
import re

def get_soup(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser", from_encoding='euc-kr')
    return soup

def get_price(company_code):
    soup = get_soup(company_code)
    name = re.match('[\w ]+ :',  soup.find("title").text)[0][:-2]
    no_today = soup.find("p", {"class": "no_today"})
    now_price = no_today.find("span", {"class": "blind"}).text
    return name, now_price


company_codes = ["005930", "017670", "402340", "035720", "367380", "129890"] 


while True:
    now = datetime.now()
    print (now)
    
    for item in company_codes:
        name, now_price = get_price(item)
        print(name, "\t", now_price)
    print("-------------------------------")
    time.sleep(60)