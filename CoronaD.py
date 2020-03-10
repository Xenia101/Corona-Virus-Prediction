import matplotlib.pyplot as plt
import getData
import datetime as dt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
#from statsmodels.tsa.arima_model import ARIMA
import statsmodels

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
    edit_data = data.diff(periods=1).iloc[1:]
    plot_acf(data)
    plot_pacf(data)
    plt.show()
    # p = 0, q = 1

def ARIMA():
    series = pd.read_csv('./data/data.csv', header=0, index_col=0, squeeze=True)
    order = (0,1,1)
    model = statsmodels.tsa.arima_model.ARIMA(series, order, freq='D')
    model_fit = model.fit(trend='nc',full_output=True, disp=1)
    print(model_fit.summary())
    plt = model_fit.plot_predict()
    plt.show()
    fore = model_fit.forecast(steps=1)
    print(fore)
    
if __name__ == "__main__":
    data = getData.read_csv('list')
    ShowGraph(data)

    Calc_ACF_PAF()
    ARIMA()
