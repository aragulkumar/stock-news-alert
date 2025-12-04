# 📈 Stock News Alert – Day 36 of 100 Days of Code

This project automatically checks the stock price of a chosen company and, if there is a significant change in price, it fetches the latest related news articles and sends them as alerts via SMS/email.

I built this as part of the **100 Days of Code (Day 36)** to practice working with **APIs, JSON data, environment variables, and automation**.

---

## 🚀 Features

- Monitors daily price change of a selected stock (e.g., TSLA, AAPL, etc.).
- Uses a stock price API to get recent closing prices.
- Calculates percentage change between today and yesterday.
- If the change crosses a defined threshold (e.g., ±5%), it:
  - Fetches top company-related news headlines.
  - Sends alerts with headline + brief description via SMS (Twilio) or email.
- Uses environment variables for API keys and secrets (no hard-coded keys).
- Can be scheduled to run automatically (e.g., using cron / PythonAnywhere).

---

## 🧠 Tech Stack

- **Language:** Python
- **APIs:** Stock price API, News API (e.g., Alpha Vantage, NewsAPI)
- **Notifications:** Twilio SMS / email (SMTP)
- **Environment:** Tested on Linux (WSL / Ubuntu)
- **Automation (optional):** Cron job / PythonAnywhere

---

## 📂 Project Structure

```bash
stock-news-alert/
│── main.py                  # Main script to run the alert logic
│── stock_manager.py         # Handles fetching stock data (optional)
│── news_manager.py          # Handles fetching news data (optional)
│── notification_manager.py  # Handles sending SMS/email (optional)
│── .env.example             # Sample environment variables (no real keys)
│── requirements.txt         # Python dependencies
│── .gitignore               # Ignore venv, .env, cache files, etc.
│── README.md                # Project documentation
