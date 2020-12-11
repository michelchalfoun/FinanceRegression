import requests
import json

apiKey = "d64e47f7b3b94ffa5e7ebe1ba396ceb0"

financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/financial-ratios/AAPL?apikey=" + apiKey)
financial_ratios = financial_ratios.json()

print(financial_ratios)
