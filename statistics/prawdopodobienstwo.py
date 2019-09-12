import scipy.stats as stats
import numpy as np

s = 100 # średnia
v = 50 # wariancja
sq = np.sqrt(v) # odchylenie standardowe
print(sq)
print("Prawdopodobieństwo, że zostanie uzyskany wynik poniżej 110 wynosi"\
, round(stats.norm(s, sq).cdf(110), 4))
print("Prawdopodobieństwo, że zostanie uzyskany wynik powyzej 110 wynosi"\
, 1 - round(stats.norm(s, sq).cdf(110), 4))
print("Prawdopodobieństwo, że zostanie uzyskany wynik pomiędzy 90 a 115 wynosi"\
      , round(stats.norm(s, sq).cdf(115), 4) - round(stats.norm(s, sq).cdf(90), 4))
print("Prawdopodobieństwo, że zostanie uzyskany wynik poniżej 90 lub powyżej 115 wynosi"\
      , round(1 - stats.norm(s, sq).cdf(115)+ stats.norm(s, sq).cdf(90), 4))
