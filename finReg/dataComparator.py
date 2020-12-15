import numpy as np
import json
import dataHandler as dh

# Retrieves the API key needed to process the http request
with open("config.json") as json_data_file:
    data = json.load(json_data_file)
    apiKey = data['FinancialModeling']['apiKey']

def compareRatioSlopes(ticker, basisRatio, comparableRatios):
    
    # Get data needed for the basis ratio
    basisYears, basisRatios = dh.getRatios(ticker, basisRatio, apiKey)

    # Checks if data was found for this ratio
    if (basisYears == []):
        print("No data for basis ratio:", basisRatio)
        return
    else:

        # Shows the slope of the regresion of the basis ratio for visualization
        basisM = np.polyfit(basisYears, basisRatios, 1)[0]
        print("The slope of", basisRatio, "is:", basisM)
        difference = float(input("Enter the maximum difference allowed for slop comparison: "))
        foundRatios = []

        for i in comparableRatios:

            # Gets the data needed for each ratio in order to compare
            years, ratios = dh.getRatios(ticker, i, apiKey)

            if (years != []):
                # Find coefficients of the Least Squares Regression
                comparableM = np.polyfit(years, ratios, 1)[0]

                # Compute individual points of the regression for plotting
                topBound = basisM + difference
                bottomBound = basisM - difference
                
                # Compares slopes to return the ratios that meet the conditions
                if (bottomBound < comparableM < topBound):
                    if (np.sign(comparableM) == np.sign(basisM)):
                        foundRatios.append(i)

        return foundRatios