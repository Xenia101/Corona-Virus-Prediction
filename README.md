# Corona-Virus-Prediction

Time series analysis with Corona Virus Daily Data and ARIMA models

## Example

1. Use ```getData.py``` to bring ```./data/data.csv``` 
[Corona virus daily status Dataset](https://github.com/Xenia101/Korean-Data-Set/tree/master/Corona%20virus%20daily%20status)

2. Show a Data Graph

```python
data = getData.read_csv('list')

def ShowGraph(data):
  df = pd.DataFrame(data, columns = ['date' , 'value'])
  df.date = pd.to_datetime(df.date)
  df.value = pd.to_numeric(df['value'])
  df = df.set_index('date')
  g = df['value'].plot(title="Corona-Virus Daily data")
  plt = g.get_figure()
  ...
```

<p align=center>
  <img width="500px" src="https://github.com/Xenia101/Corona-Virus-Prediction/blob/master/img/Figure_1.png?raw=true">
</p>

3. **ACF** & **PAF** Calculation and Show a graphs

```python
def Calc_ACF_PAF():
  ...
  plot_acf(data)
  plot_pacf(data)
  ...
```

<p align=center>
  <img width="400px" src="https://github.com/Xenia101/Corona-Virus-Prediction/blob/master/img/ACF.png?raw=true">
  <img width="400px" src="https://github.com/Xenia101/Corona-Virus-Prediction/blob/master/img/PACF.png?raw=true">
</p>

> Left : ACF / Right : PACF

4. 

## Execution / Test Environment

- Window 10
- Python **3.6**
