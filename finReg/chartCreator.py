import matplotlib.pyplot as plt
import json
import dataHandler as dh

# Retrieves the API key needed to process the http request
with open("config.json") as json_data_file:
    data = json.load(json_data_file)
    apiKey = data['FinancialModeling']['apiKey']

# Plot a one or multiple ratios given an array of ratios
def plotRatios(ticker, profitabilityRatios):
    for i in profitabilityRatios:
        years, ratios = dh.getRatios(ticker, i, apiKey)
        plt.plot(years, ratios, label=i)

    if (len(profitabilityRatios) == 1):
        plt.title(profitabilityRatios[0] + " of " + ticker + " per year")
    else:
        plt.title("Profitability ratios of " + ticker + " per year")
        plt.legend(loc='upper right')
    plt.show()