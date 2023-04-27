'''
When the price of certain stock goes down than the [threshold], send a message through a telegram bot.
author: jhpark@robotics.snu.ac.kr
'''
from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
import re
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler 

# Stock to take a look
company_code = "367380"  # ACE NASDAQ100
# company_code_abko = "129890" # ABKO

threshold = 13000


bot = telegram.Bot(token="thetelegrambotoken123456789:abcdefg")
chat_id = "somechatid123456789"

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

def send_alarm():
    now = datetime.now()
    print(now)
    
    name, current_price = get_price(company_code)
    print(name, "\t", current_price)
    print("-------------------------------")
    
    # If price gets lower than the [threshold], telegram bot sends an alert. BUY NOW!
    if int(current_price.replace(",","")) < threshold:
        alert_message = "{}        current price: \n{}                  < threshold: {}\n\nIT IS TIME TO BUY!".format(name, current_price, threshold)
        bot.sendMessage(chat_id=chat_id, text=alert_message)
        print(alert_message)
        print("ALARM HAS SENT!!!")
    # when price > [threshold]
    else:
        waiting_message = "{}        current price: \n{}                  > threshold: {}\n\nWait!".format(name, current_price, threshold)
        # bot.sendMessage(chat_id=chat_id, text=waiting_message)
        print(waiting_message)    
    





if __name__=="__main__":
    send_alarm()
               
sc = BlockingScheduler()
sc.add_job(send_alarm, 'interval', seconds = 3600)
sc.start()
