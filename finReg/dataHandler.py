import requests
import json

# getRatio returns a specific ratio in a specific year and quarter
def getRatio(ticker, ratio, year, quarter, apiKey):

    # Perform the request to the API to retreive all ratios for ticker quarterly
    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/ratios/" + ticker +"?period=quarter&apikey=" + apiKey)
    financial_ratios = financial_ratios.json()

    for i in reversed(range(len(financial_ratios))):
        
        # Splits date values to simplify comparisons
        splitDate = financial_ratios[i]['date'].split("-")
        
        # Checks if data is non existant
        if (str(year) == splitDate[0]) and ((quarter * 3) == int(splitDate[1])):
            return financial_ratios[i][ratio]
    
    return False

# getRatios returns a specific profitability ratio in all the years available
def getRatios(ticker, ratio, apiKey):

    # Perform the request to the API to retreive all ratios for ticker quarterly
    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/ratios/" + ticker +"?period=quarter&apikey=" + apiKey)
    financial_ratios = financial_ratios.json()
    years = []
    ratios = []

    for i in reversed(range(len(financial_ratios))):
        
        # Checks if data is non existant
        if (financial_ratios[i][ratio] != '') and (financial_ratios[i][ratio] != None):
            
            # Splits date values to simplify comparisons
            splitDate = financial_ratios[i]['date'].split("-")
            
            # Compute quarters as 0, 0.25, 0.5, 0.75 of years
            years.append(float(splitDate[0]) + (float(splitDate[1]) / (12)) - 0.25)
            ratios.append(float(financial_ratios[i][ratio]))
    
    return years, ratios

# getAllRatios returns all profitability ratios in all the years available
def getAllRatios(ticker, apiKey):

    # Perform the request to the API to retreive all ratios for ticker quarterly
    financial_ratios =  requests.get(f"https://financialmodelingprep.com/api/v3/ratios/" + ticker +"?period=quarter&apikey=" + apiKey)
    financial_ratios = financial_ratios.json()
    years = []
    profitRatios = []

    for i in reversed(range(len(financial_ratios))):
        
        # Splits date values to simplify comparisons
        splitDate = financial_ratios[i]['date'].split("-")
        
        # Compute quarters as 0, 0.25, 0.5, 0.75 of years
        years.append(float(splitDate[0]) + (float(splitDate[1]) / (12)) - 0.25)
        
        # Removes unnecessary values from dict
        editedRatioDict = financial_ratios[i]
        del editedRatioDict['symbol']
        del editedRatioDict['date']
        profitRatios.append(editedRatioDict)
    
    return years, profitRatios