# -*- coding: utf-8 -*-

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-4,6,100)

plt.figure()
plt.plot(x,stats.norm.pdf(x),"r")
plt.title("Rozkład normalny")
plt.show()

plt.figure()
plt.plot(x,stats.uniform.pdf(x),"k")
plt.title("Rozkład jednostajny")
plt.show()

plt.figure()
plt.plot(x,stats.expon.pdf(x),"m")
plt.title("Rozkład wykładniczy")
plt.show()

plt.figure()
plt.plot(x,stats.gamma.pdf(x,a=2),"y")
plt.title("Rozkład gamma")
plt.show()

plt.figure()
plt.plot(x,stats.beta.pdf(x,a=0.5,b=3),"b")
plt.title("Rozkład beta")
plt.show()

plt.figure()
plt.plot(x,stats.chi2.pdf(x,df=6),"k")
plt.title("Rozkład $\chi^2$")
plt.show()

plt.figure()
plt.plot(x,stats.t.pdf(x,df=8),"g")
plt.title("Rozkład t-Studenta")
plt.show()

plt.figure()
plt.plot(x,stats.f.pdf(x,dfn=2,dfd=7),"m")
plt.title("Rozkład F-Snedecora")
plt.show()

plt.figure()
plt.plot(x,stats.cauchy.pdf(x),"r")
plt.title("Rozkład Cauchy'ego")
plt.show()


# cdf() - dystrybuanta

# pdf() - gęstosc rozkładu prawdopodobieństwa

# sf() - funkcja przeżycia (1-cdf)

# logcdf() - logarytm dystrybuanty

# logpdf() - lodarytm gęstosci

# logsf() - logarytm funkcji przeżycia

# ppf() - percentyle teoretyczne (odwrotnosc dystrybuanty)

# median() - mediana

# mean() - wartosc oczekiwana

# var() - wariancja

# std() - odchylenie standardowe

#stats() - wartosc oczekiwana, wariancja, skosnosc, kurtoza (moments="w,v,s,k")





























