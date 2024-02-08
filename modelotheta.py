# -*- coding: utf-8 -*-
"""ModeloTheta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14a_nG-fBsNoaXiLPlpIJ0wAyFasYpJiU

Modelo Theta
"""

#Instale, se necessário, na versão sugerida
!pip install statsmodels==0.13.5

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc("figure",figsize=(12,6))
plt.rc("font",size=15)
plt.rc("lines",linewidth=2)
sns.set_style("darkgrid")

df = pd.read_csv('/content/TabelaSojaIBGE.csv',sep=";", index_col=0, parse_dates=True)
df.head()

df['SojaProduzida'].plot();

df.index

idx = pd.date_range(start=df.index.min(), end=df.index.max(), freq='B')
df = df.reindex(idx)
df.fillna(method='ffill', inplace=True)

from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import pyplot

result = seasonal_decompose(df['SojaProduzida'], model='multiplicative', period=7)
result.plot()

pyplot.show()

from statsmodels.tsa.forecasting.theta import ThetaModel
tm = ThetaModel(df['SojaProduzida'])
res = tm.fit()
print(res.summary())

res = ThetaModel(df['SojaProduzida'],deseasonalize=True,period=5).fit()
fcast = res.forecast(24)

plt.figure(figsize = (12,6))

plt.plot(fcast,  color = 'red', label = 'Forecast')
plt.plot(df['SojaProduzida'],color = 'blue', label = 'Observed data')


plt.title('Standard Theta Model')
plt.legend()
plt.show()

tm = ThetaModel(df['SojaProduzida'], method="multiplicative")
res = tm.fit(use_mle=True)
print(res.summary())

ax = res.plot_predict(24, theta=2)