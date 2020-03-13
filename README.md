# Corona-Virus-Prediction

Time series analysis with Corona Virus Daily Data and ARIMA models

### ARIMA(Autoregressive integrated moving average) 란?
> In statistics and econometrics, and in particular in time series analysis, an autoregressive integrated moving average (ARIMA) model is a generalization of an autoregressive moving average (ARMA) model. Both of these models are fitted to time series data either to better understand the data or to predict future points in the series (forecasting).
[WIKIPEDIA](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average)

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

4. Forecast using **ARIMA** models

```python
def ARIMA():
  ...
  order = (0,1,1)
  model = statsmodels.tsa.arima_model.ARIMA(series, order, freq='D')
  model_fit = model.fit(trend='c',full_output=True, disp=10)
  ...
```

5. Show a graph

```python
def ARIMA():
  ...
  plt = model_fit.plot_predict()
  Number_to_predict = 3
  fore = model_fit.forecast(steps=Number_to_predict)
  ...
```

<p align=center>
  <img width="500px" src="https://github.com/Xenia101/Corona-Virus-Prediction/blob/master/img/predict.png?raw=true">
</p>

> Orange Line : Origin / Blue Line : Forecast

6. Result

```python
for x in fore[0]:
        p_time = time + timedelta(days=Number_to_predict)
        p_time = p_time.strftime('%Y-%m-%d')
        print("{0} : {1}".format(p_time, x))
        Number_to_predict += 1
```
```json
# Output
2020-03-09 : 6057.29830482379
2020-03-10 : 6196.215619909736
2020-03-11 : 6335.132934995682
```

## Differences between **actual data** and **forecast results**

|날짜|Predict|Actuality|Difference|
|------|:---:|:---:|:---:|
|2020-03-09|6057|7382|1325|
|2020-03-10|6196|7513|1317|
|2020-03-11|6335|7755|1420|

## Execution / Test Environment

- Window 10
- Python **3.6**
