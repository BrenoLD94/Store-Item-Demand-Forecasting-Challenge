# importando as bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from sklearn.utils import shuffle

def rolling(timeseries, anoInicial = 2013, anoFinal = 2017):
    """
        Plota a média e variância de uma série temporal
        
        params: 
         - timeseries: Serie object com o index como dateTime;
         - anoInicial: Inteiro;
         - anoFinal: Inteiro.
    """
    media = []
    std = []
    for ano in range(anoInicial, anoFinal):
        tsTemp = timeseries[str(ano):str(ano+1)]
        media.append(tsTemp.mean())
        std.append(tsTemp.std())
    
    x = [x for x in range(anoInicial, anoFinal)]
    
    plt.figure(figsize=(12, 7))
    plt.title("Variação da média e do desvio padrão ao longo dos anos")
    plt.xlabel('Ano')
    plt.ylabel("Variação")
    
    plt.plot(x, media, c='darkGreen', label='Média')
    plt.plot(x, std, c='darkRed', label='Desvio Padrão')
    
    plt.grid(True)
    plt.legend()
    plt.show()



def converterParaEstacionario(dataOriginal):
    data = dataOriginal.copy()
    storeSize = data.store.max()
    itemSize = data.item.max()
    listaData = []
    
    for storeIndice in range(1, storeSize+1):
        dTemp = data[data.store == storeIndice]
        for itemIndice in range(1, itemSize+1):
            dTemp2 = dTemp[dTemp.item == itemIndice].sales.diff().shift(-1)
            tamanho = len(dTemp2)
        
            myDict = {"store": [storeIndice for x in range(0, tamanho)],
                      "item": [itemIndice for x in range(0, tamanho)],
                      "sales_F": dTemp2.values,
                      "date": dTemp2.index}
        
            listaData.append(pd.DataFrame(myDict))
        
    newDataFrame = pd.concat(listaData)
    newDataFrame['sales'] = np.array(dataOriginal.sales)
    newDataFrame.set_index('date', inplace = True)

    return shuffle(newDataFrame)


def addNewColumns(data):
    calendario = pd.Series(data.index)
    
    data['ano'] = np.array(calendario.dt.year)
    data['mes'] = np.array(calendario.dt.month)
    data['dia'] = np.array(calendario.dt.day)
    data['diaSemana'] = np.array(calendario.dt.dayofweek)
    data['trimestre'] = np.array(calendario.dt.quarter)
    
    return data


# função que unifica todas as transformações
def formatoIdeal(dataOriginal, isDataTeste = False):
    data = dataOriginal.copy()
    
    if not isDataTeste:
        data['sales_F'] = data['sales'].apply(lambda x: np.sqrt(x))
        data.drop(['sales'], axis = 1, inplace = True)

    newData = addNewColumns(data)
    newData.dropna(how="any", axis = 0, inplace = True)

    return newData
