import chartCreator as cc
import dataHandler as dh
from pprint import pprint

# This function plots the data ratios needed for the ticker
ticker = "AAPL"
cc.plotRatios(ticker, ["grossProfitMargin", "netProfitMargin", "effectiveTaxRate"])
years, values = dh.getAllRatios("TSLA", "d64e47f7b3b94ffa5e7ebe1ba396ceb0")
pprint(values)
