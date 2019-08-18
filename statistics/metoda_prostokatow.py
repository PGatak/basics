import numpy as np


def f(x):
    return np.arctan(x)


a = float(input("Podaj punkt poczatkowy: "))
b = float(input("Podaj punkt końcowy: "))
N = int(input("Podaj liczbę iteracji: "))

dl = (b-a)/N

calka = 0

z = a
for i in range(1,N+1):
    z += dl
    calka = calka + f(z)*dl

print("Wartosc calki wynosi: ",round(calka, 5))

