import chartCreator as cc
import dataHandler as dh

ticker = "AMZN"
ratios = ["grossProfitMargin", "cashRatio"]
cc.plotLinSquareRegression(ticker, ratios, True)

