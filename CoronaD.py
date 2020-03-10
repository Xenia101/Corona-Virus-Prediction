import matplotlib.pyplot as plt
import getData
import datetime as dt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def ShowGraph(data): # Show data Graph
    df = pd.DataFrame(data, columns = ['date' , 'value'])
    df.date = pd.to_datetime(df.date)
    df.value = pd.to_numeric(df['value'])
    df = df.set_index('date')
    g = df['value'].plot(title="Corona-Virus Daily data")
    plt = g.get_figure()
    plt.show()

def Calc_ACF_PAF(): # ACF PAF Calculation with ARIMA models
    data = pd.read_csv('./data/data.csv', header=0, index_col=0, squeeze=True)
    plot_acf(data)
    plot_pacf(data)
    plt.show()
    
if __name__ == "__main__":
    data = getData.read_csv('list')
    #ShowGraph(data)
    Calc_ACF_PAF()

#https://byeongkijeong.github.io/ARIMA-with-Python/
