import matplotlib.pyplot as plt
import getData
import datetime as dt
import pandas as pd

def ShowGraph(data):
    df = pd.DataFrame(data, columns = ['date' , 'value'])
    df.date = pd.to_datetime(df.date)
    df.value = pd.to_numeric(df['value'])
    df = df.set_index('date')
    g = df['value'].plot(title="Corona-Virus Daily data")
    plt = g.get_figure()
    plt.show()

if __name__ == "__main__":
    data = getData.read_csv('list')
    ShowGraph(data)

#https://byeongkijeong.github.io/ARIMA-with-Python/
