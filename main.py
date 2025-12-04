import os
from twilio.rest import Client
import requests


STOCK = "ITC"
COMPANY_NAME = "ITC Ltd"


# NEWS_API_KEY=
# TWILIO_SID=
# TWILIO_AUTH_TOKEN=
# TWILIO_PHONE=+1XXXXXXXXXX
# TARGET_PHONE=+91XXXXXXXXXX

STOCK_API_KEY="STOCK_API_KEY"
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TARGET_PHONE_NUMBER = os.getenv("TARGET_PHONE_NUMBER")


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK_API_Endpoint = "https://www.alphavantage.co/query"

STOCK_PARAMS = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"ITC.BSE",
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,

}






response = requests.get(STOCK_API_Endpoint,STOCK_PARAMS)
data = response.json()

print(data["Time Series (Daily)"]["2025-12-02"]["1. open"])
print(data["Time Series (Daily)"]["2025-12-03"]["1. open"])


















## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

