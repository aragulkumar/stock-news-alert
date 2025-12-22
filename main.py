import requests
import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_number = os.environ["TWILIO_PHONE_NUMBER"]
target_number = os.environ["TARGET_PHONE_NUMBER"]

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY="LtdYBSE60PK0T8UDWR1"
NEWS_API_KEY="d002bb868d0b465e887aa549e8c6d220"

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#Get yesterday's closing stock price. 

stock_params = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey':STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday = data_list[0]
yesterday_closing_price = yesterday["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = (difference / float(day_before_yesterday_closing_price)) * 100
print(diff_percent)


#If percentage is greater than 5 then print("Get News").
#get the first 3 news pieces for the COMPANY_NAME. 

if diff_percent > 5:
    news_params = {
        "apiKey":NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        
    }
    response = requests.get(NEWS_ENDPOINT,params= news_params)
    articles = response.json()["articles"]

#to send a separate message with each article's title and description to your phone number.
    three_articles = articles[:3]

#Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [ f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
  
    
#Send each article as a separate message via Twilio. 
    client = Client(account_sid, auth_token)

    emoji = "🔺" if float(yesterday_closing_price) > float(day_before_yesterday_closing_price) else "🔻"
    header = f"{STOCK_NAME}: {emoji}{diff_percent:.2f}%"

    full_message = header + "\n\n" + "\n\n".join(formatted_articles)

#Works only Twilio paid version because of long msg.
    message = client.messages.create(
        body=full_message,
        from_=twilio_number,
        to=target_number,
    )

#Sending through Mail 
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_TO
    msg["Subject"] = f"{STOCK_NAME} Stock News Alert"

    # Send your existing full_message as email content

    msg.set_content(full_message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print("Mail sent successfully")
            

