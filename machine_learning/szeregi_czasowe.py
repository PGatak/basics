# -*- coding: utf-8 -*-

from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.arima_model import ARMA
from random import random
import matplotlib.pyplot as plt
import math

# AR(p)

data = [math.sin(x) + 0.25*random() for x in range(300)]
train_data = data[:150]
test_data = data[150:]

model = AR(train_data)
model_fit = model.fit()

y = model_fit.predict(len(train_data),len(data)-1)

plt.figure(figsize = (16,8))
plt.title('Porównanie danych z przewidywaniami modelu AR')
plt.plot(range(len(test_data)),test_data,'k',label = 'Dane testowe')
plt.plot(range(len(y)),y,'r',label = 'AR')
plt.legend()
plt.axis([0,20,-2,2])
plt.show()

# MA(q)

model1 = ARMA(train_data, order=(0, 1,))
model_fit1 = model1.fit(disp=False)

y1 = model_fit1.predict(len(train_data),len(data)-1)
  
plt.figure(figsize = (16,8))
plt.title('Porównanie danych z przewidywaniami modelu MA')
plt.plot(range(len(test_data)),test_data,'k',label = 'Dane testowe')
plt.plot(range(len(y1)),y1,'r',label = 'MA')
plt.legend()
plt.axis([0,20,-2,2])
plt.show() 




























