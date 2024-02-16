from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
import matplotlib.pyplot as plt
import  seaborn as sns
from time import time
from time import sleep

from urllib3.filepost import writer

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ee16a5d6-1767-4193-a759-8e939a20b9ac',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  # print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# This normalizes the data and makes it all pretty in a dataframe
df = pd.json_normalize(data["data"])

# To add a new column to register the time stamps
df["timestamps"] = pd.to_datetime("now")

# This saves the dataframe in an Excel file
if not os.path.isfile(r"D:\TRY IT(Data Analysis)\SortingTrials\APITrials.xlsx"):
    df.to_csv(r"D:\TRY IT(Data Analysis)\SortingTrials\APITrials.csv", header="column names", index=False)
else:
    df.to_csv(r"D:\TRY IT(Data Analysis)\SortingTrials\APITrials.csv", mode="a", header=False, index=False)


def api_runner():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '20',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee16a5d6-1767-4193-a759-8e939a20b9ac',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        # print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    pd.set_option("display.max_columns", None)

    df = pd.read_csv(r"D:\TRY IT(Data Analysis)\SortingTrials\APITrials.csv")

    # This normalizes the data and makes it all pretty in a dataframe
    df2 = pd.json_normalize(data["data"])

    # To add a new column to register the time stamps
    df2["timestamps"] = pd.to_datetime("now")

    # This updates df in the Excel file
    df = df._append(df2)
    # This saves the dataframe in an Excel file
    df.to_csv(r"D:\TRY IT(Data Analysis)\SortingTrials\APITrials.csv", mode="a", index=False)


for i in range(2):
    api_runner()
    print("API Runner Completed")
    sleep(1)


pd.set_option("display.float", lambda x: "%.5f" % x)

df3 = df.groupby("name", sort=False)[["quote.USD.percent_change_1h", "quote.USD.percent_change_24h","quote.USD.percent_change_7d", "quote.USD.percent_change_30d"]].mean()

df4 = df3.stack()
df5 = df4.to_frame(name="values")

index = pd.Index(range(df4.count()))
df6 = df5.reset_index()

df7 = df6.rename(columns={"level_1": "percent_change"})
df7["percent_change"] = df7["percent_change"].replace(["quote.USD.percent_change_1h","quote.USD.percent_change_24h","quote.USD.percent_change_7d", "quote.USD.percent_change_30d"],["1h","24h","7d","30d"])
(print("\n"))
print(df7)

sns.catplot(x="percent_change", y="values", hue="name", data=df7, kind="point")

plt.show()