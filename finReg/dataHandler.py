import requests
import json

# getRatio returns a specific ratio in a specific year and quarter
def getRatio(ticker, ratio, year, quarter, apiKey):

    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/ratios/" + ticker +"?period=quarter&apikey=" + apiKey)
    financial_ratios = financial_ratios.json()

    for i in reversed(range(len(financial_ratios))):
        splitDate = financial_ratios[i]['date'].split("-")
        if (str(year) == splitDate[0]) and ((quarter * 3) == int(splitDate[1])):
            return financial_ratios[i][ratio]
    
    return False

# getRatio returns a specific profitability ratio in all the years available
def getRatios(ticker, ratio, apiKey):

    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/ratios/" + ticker +"?period=quarter&apikey=" + apiKey)
    financial_ratios = financial_ratios.json()
    years = []
    ratios = []

    for i in reversed(range(len(financial_ratios))):
        if (financial_ratios[i][ratio] != '') and (financial_ratios[i][ratio] != None):
            splitDate = financial_ratios[i]['date'].split("-")
            years.append(float(splitDate[0]) + (float(splitDate[1]) / (12)) - 0.25)
            ratios.append(float(financial_ratios[i][ratio]))
    
    return years, ratios

# getRatio returns all profitability ratios in all the years available
def getAllRatios(ticker, apiKey):

    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/ratios/" + ticker +"?period=quarter&apikey=" + apiKey)
    financial_ratios = financial_ratios.json()
    years = []
    profitRatios = []

    for i in reversed(range(len(financial_ratios))):
        splitDate = financial_ratios[i]['date'].split("-")
        years.append(float(splitDate[0]) + (float(splitDate[1]) / (12)) - 0.25)
        editedRatioDict = financial_ratios[i]
        del editedRatioDict['symbol']
        del editedRatioDict['date']
        profitRatios.append(editedRatioDict)
    
    return years, profitRatios