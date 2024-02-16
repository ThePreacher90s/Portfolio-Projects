# Import Libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import smtplib
import time
import datetime

# Connect to a websites
url = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(url, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = soup2.find(id="productTitle").getText().strip()

today = datetime.date.today()
price = (f"{soup2.find(class_="a-price-symbol").getText().strip()}"
         f"{soup2.find(class_="a-price-whole").get_text(strip=True)}"
         f"{soup2.find(class_="a-price-fraction").getText().strip()}"
         )
price = price.strip()[1:]
print(title)
print(price)

header = ["Title", "Price", "Date"]
data = [title, price, today]

with open("AmazonWebScrapperDataSet.csv", "w", newline="", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

print("\n")
df = pd.read_csv(r"C:\Users\RUFUS BOLU\PycharmProjects\HelloWorld\pythonProject\AmazonWebScrapperDataSet.csv")
print(df)

#Now we are appending data to the csv
with open("AmazonWebScrapperDataSet.csv", "a+", newline="", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(data)


def check_price():
    url = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id="productTitle").getText().strip()
    today = datetime.date.today()
    price = (f"{soup2.find(class_="a-price-symbol").getText().strip()}"
             f"{soup2.find(class_="a-price-whole").get_text(strip=True)}"
             f"{soup2.find(class_="a-price-fraction").getText().strip()}"
             )
    price = price.strip()[1:]
    print(title)
    print(price)
    header = ["Title", "Price", "Date"]
    data = [title, price, today]
    with open("AmazonWebScrapperDataSet.csv", "a+", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(data)


x: int = 0
while x < 3:
    check_price()
    time.sleep(5)
    x += 1

print(df)