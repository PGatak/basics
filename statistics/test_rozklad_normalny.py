# -*- coding: utf-8 -*-

import seaborn as sns
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

tips = sns.load_dataset('tips')
print(tips.head())

tips['logtip'] = np.log(tips.tip)
m, s = sp.stats.norm.fit(tips.logtip)

print ('Wartosc srednia wynosi %s a odchylenie standardowe %s.' % (round(m,3),round(s,3)))

plt.figure()
plt.subplot(121)
plt.axis([-0.5, 3, 0, 1])
ecdf = ECDF(tips.logtip)
plt.step(ecdf.x, ecdf.y, 'r-', label = r'$\hat{F}_n(x)$')

t1 = np.linspace(-0.5, 3, 100)
t2 = sp.stats.norm.cdf(t1, loc = m, scale = s)
t3 = sp.stats.norm.pdf(t1, loc = m, scale = s)
plt.plot(t1, t2, 'b--', label = r'$\mathrm{N}(%.2f, %.2f)$' % (m, s))
plt.legend(loc = 'best')

plt.subplot(122)
sns.distplot(tips.logtip, bins = 8, color = 'k')
plt.plot(t1, t3, 'g--')
plt.show()

plt.figure()
sp.stats.probplot(tips.logtip, dist = sp.stats.norm, plot = plt)

test1 = sp.stats.skewtest(tips.logtip)        # test skosnosci H0: skosnosc = 0, H1: skosnosc != 0

print('Wartosc statystyki testowej: %s a p-value: %s' %(round(test1.statistic,4),round(test1.pvalue,4)))

test2 = sp.stats.kurtosistest(tips.logtip)   # test kurtozy H0: kurtoza = 3, H1: kurtoza != 3

print('Wartosc statystyki testowej: %s a p-value: %s' %(round(test2.statistic,4),round(test2.pvalue,4)))

test3 = sp.stats.shapiro(tips.logtip)   # test Shapiro - Wilka (sprawdza jednoczesnie kurtoze i skosnosc)

print('Wartosc statystyki testowej: %s a p-value: %s' %(round(test3[0],4),round(test3[1],4)))

test4 = sp.stats.kstest(tips.logtip, 'norm', args = (m, s)) # test Kołomogorowa - Smirnowa porownuje dystrybuanty

print('Wartosc statystyki testowej: %s a p-value: %s' %(round(test4.statistic,4),round(test4.pvalue,4)))


















