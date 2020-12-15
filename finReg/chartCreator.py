import matplotlib.pyplot as plt
import numpy as np
import json
import dataHandler as dh

# Retrieves the API key needed to process the http request
with open("config.json") as json_data_file:
    data = json.load(json_data_file)
    apiKey = data['FinancialModeling']['apiKey']

# Plot one or multiple ratios given an array of ratios
def plotRatios(ticker, profitabilityRatios):
    
    # Get ratios and plot them as individual points with labeling
    for i in profitabilityRatios:
        years, ratios = dh.getRatios(ticker, i, apiKey)
        plt.plot(years, ratios, label=i)

    # Chooses title based on number of passed in ratios
    if (len(profitabilityRatios) == 1):
        plt.title(profitabilityRatios[0] + " of " + ticker + " per year")
    else:
        plt.title("Profitability ratios of " + ticker + " per year")
        plt.legend(loc='upper right')
    plt.show()

# Plot the regressions of one or multiple ratios given an array of ratios
def plotLinSquareRegression(ticker, profitabilityRatios, visualizeWithPoints:bool, plot:bool):
    
    # Computes Least Squares Regression for the given ratios
    for i in profitabilityRatios:
        years, ratios = dh.getRatios(ticker, i, apiKey)

        if (years == []):
            print("No data for ratio:", i)
        else:
            # Find coefficients of the Least Squares Regression
            m, c = np.polyfit(years, ratios, 1)

            # Compute individual points of the regression for plotting
            xn = np.linspace(years[0], years[len(years) - 1], 200)
            yn = np.polyval([m, c], xn)
            plt.plot(xn, yn, label=(i + " LS regression"))

            # Shows the individual points before the regression if requested
            if(visualizeWithPoints):
                plt.plot(years, ratios, label=i)

    # Chooses title based on number of passed in ratios
    if (len(profitabilityRatios) == 1):
        plt.title(profitabilityRatios[0] + " least squares fit of " + ticker + " per year")
    else:
        plt.title("Profitability ratios least squares fit of " + ticker + " per year")
        plt.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1)

    if (plot):
        plt.show()
