import chartCreator as cc
import dataHandler as dh
import dataComparator as dc
import json

ticker = "MSFT"
basisRatio = 'grossProfitMargin'
ratioNames = dh.getRatioNames("d64e47f7b3b94ffa5e7ebe1ba396ceb0")

ratioNames.remove(basisRatio)
foundRatios = dc.compareRatioSlopes(ticker, basisRatio, ratioNames) 

ratiosToPlot = foundRatios
ratiosToPlot.insert(0, basisRatio) 

cc.plotLSquareRegression(ticker , ratiosToPlot, True, True)