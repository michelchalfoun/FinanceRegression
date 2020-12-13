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
    years = []
    ratios = []

    for i in reversed(range(len(financial_ratios['ratios']))):
        if (financial_ratios['ratios'][i]['profitabilityIndicatorRatios'][profitabilityRatio] != ''):
            years.append(int(financial_ratios['ratios'][i]['date'][0:4]))
            ratios.append(float(financial_ratios['ratios'][i]['profitabilityIndicatorRatios'][profitabilityRatio]))
    
    return years, ratios

# getRatio returns all profitability ratios in all the years available
def getAllRatios(ticker, apiKey):

    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/financial-ratios/" + ticker +"?apikey=" + apiKey)
    financial_ratios = financial_ratios.json()
    years = []
    profitRatios = []

    for i in reversed(range(len(financial_ratios['ratios']))):
        years.append(financial_ratios['ratios'][i]['date'][0:4])
        profitRatios.append(financial_ratios['ratios'][i]['profitabilityIndicatorRatios'])
    
    return years, profitRatios