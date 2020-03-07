import matplotlib.pyplot as plt
import getData
import datetime as dt
import pandas as pd

data = getData.read_csv('list')
df = pd.DataFrame(data, columns = ['date' , 'value'])
df.set_index('date', inplace=True)

plt.plot(df.index, df.value, marker='s', color='r')
plt.show()
