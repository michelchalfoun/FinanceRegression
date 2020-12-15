import chartCreator as cc
import dataHandler as dh
import dataComparator as dc
import json

ticker = input("Enter the ticker symbol of the company: ")
basisRatio = input("Enter the basis ratio: ")

foundRatios = dc.compareRatioSlopes(ticker, basisRatio) 

ratiosToPlot = foundRatios
ratiosToPlot.insert(0, basisRatio) 

cc.plotLSquareRegression(ticker , ratiosToPlot, False)