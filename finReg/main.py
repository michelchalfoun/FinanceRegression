import chartCreator as cc
import dataHandler as dh
import json

ratio = "dividendPaidAndCapexCoverageRatio"

ticker = "AAPL"
ratios = ["grossProfitMargin", ratio]
# cc.plotLinSquareRegression(ticker, ratios, False, False)

ticker = "AMZN"
ratios = ["grossProfitMargin", ratio]
# cc.plotLinSquareRegression(ticker, ratios, False, False)

file = open('/Users/masenbeliveau/Desktop/FinanceRegression/finReg/test-ratios.json')
data = json.load(file)
file.close();

ratio_names = data[11]

first_ratio = "grossProfitMargin"
otherRatios = []

for (k) in ratio_names:
    if (k == "symbol" or k == "date" or k == first_ratio):
        continue
    otherRatios.append(k)

comparedRatios = cc.compareRatioSlopes("AAPL", first_ratio, otherRatios)
print(comparedRatios)
cc.plotLinSquareRegression("AAPL", comparedRatios, False, True)
for i in comparedRatios:
    temp_ratio = [first_ratio, i]
    cc.plotLinSquareRegression("AAPL", temp_ratio, False, True)