import requests
import json

# getRatio returns a specific profitability ratio in a specific year
def getRatio(ticker, profitabilityRatio, year, apiKey):

    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/financial-ratios/" + ticker +"?apikey=" + apiKey)
    financial_ratios = financial_ratios.json()

    for i in reversed(range(len(financial_ratios['ratios']))):
        if (str(year) == financial_ratios['ratios'][i]['date'][0:4]):
            return financial_ratios['ratios'][i]['profitabilityIndicatorRatios'][profitabilityRatio]
    
    return False

# getRatio returns a specific profitability ratio in all the years available
def getRatios(ticker, profitabilityRatio, apiKey):

    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/financial-ratios/" + ticker +"?apikey=" + apiKey)
    financial_ratios = financial_ratios.json()
    years = [None] * len(financial_ratios['ratios'])
    ratios = [None] * len(financial_ratios['ratios'])

    counter = 0
    for i in reversed(range(len(financial_ratios['ratios']))):
        years[counter] = int(financial_ratios['ratios'][i]['date'][0:4])
        ratios[counter] = float(financial_ratios['ratios'][i]['profitabilityIndicatorRatios'][profitabilityRatio])
        counter = counter + 1
    
    return years, ratios

# getRatio returns all profitability ratios in all the years available
def getAllRatios(ticker, apiKey):

    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/financial-ratios/" + ticker +"?apikey=" + apiKey)
    financial_ratios = financial_ratios.json()
    years = [None] * len(financial_ratios['ratios'])
    profitRatios = [None] * len(financial_ratios['ratios'])

    counter = 0
    for i in reversed(range(len(financial_ratios['ratios']))):
        years[counter] = financial_ratios['ratios'][i]['date'][0:4]
        profitRatios[counter] = financial_ratios['ratios'][i]['profitabilityIndicatorRatios']
        counter = counter + 1
    
    return years, profitRatios