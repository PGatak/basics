# -*- coding: utf-8 -*-

# Regresja liniowa:

import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as slm

X = np.array([[1], [2.3], [4.1], [6.12], [8], [10.3]]) 
Y = np.array([0.1, 0.25, 0.39, 0.59, 0.8, 1.01])

P = np.array([0.098*x + 0.006 for x in np.linspace(1,11,50)])

# Tworzymy obiekt klasy LinearRegression:

regresja = slm.LinearRegression()

regresja.fit(X,Y)
print('Wyraz wolny jest równy: %s' % round(regresja.intercept_,3))
print('Współczynnik kierunkowy wynosi: %s' % np.round(regresja.coef_,3))
print('Współczynnik dopasowania wynosi: %s' % round(regresja.score(X,Y),3))

plt.figure()
plt.scatter(X, Y, c='r', s=1.5)
plt.plot(np.linspace(1,11,50), P)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Zebrane dane')
plt.show()
