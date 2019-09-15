# -*- coding: utf-8 -*-

import numpy as np
import timeit


# Porównanie szybkoci wykonania zadania:

t1 = timeit.Timer("[math.sin(i) for i in range(10000)]","import math") # działanie na pojedyńczym elemencie obiektu
czas1 = t1.timeit(number=1000)
print("Czas wykonania pierwszego kodu wynosi:",round(czas1,4),"sekund.\n")

t2 = timeit.Timer("np.sin(np.arange(10000))","import numpy as np") # działanie na całym obiekcie
czas2 = t2.timeit(number=1000)
print("Czas wykonania drugiego kodu wynosi:",round(czas2,4),"sekund.\n")

print("***************************************************************************************************\n")

# N-wymiarową tablicę możemy utworzyć używając funkcji array() z pakietu NumPy 
# N = 1 wektor
# N = 2 macierz

x = np.array([0,1,2,3,4,5]) # wektor szescioelementowy
x1 = x.ndim                 # wymiar tablicy x
x2 = x.shape                # N-elementowa krotka okreslajaca rozmiar dla kazdego wymiaru
x3 = x.size                 # liczba wszystkich elementow
x4 = len(x)                 # liczba elementow w pierwszym wymiarze

print("Wektor:", x ,"ma wymiar:", x1 ,"i ksztalt:", x2 , end=".")
print("Liczba wszystkich jego elementow wynosi:",x3,"a liczba elementow w pierwszym wymiarze:",x4,end=".\n")

print("***************************************************************************************************\n")

# Analogicznie jak wyżej dla macierzy

A = np.array([(1,2,3),(4,5,6),(7,8,9)])
a1 = A.ndim
a2 = A.shape
a3 = A.size
a4 = len(A)

print("Macierz:", A ,"ma wymiar:", a1 ,"i ksztalt:", a2 , end=".")
print("Liczba wszystkich jej elementow wynosi:",a3,"a liczba elementow w pierwszym wymiarze:",a4,end=".\n")

print("***************************************************************************************************\n")

B = A.reshape(1,9)         # zmiana kształtu tablicy
print(B,"\n")
C = A.ravel()              # zmiana tablicy na wektor
print(C,"\n")
Cl = C.tolist()            # konwersja na liste
print(Cl,"\n")

print("***************************************************************************************************\n")

# Kilka specjalnych macierzy

print(np.arange(1,5,0.5),"\n")           # ciag liczb od 1 do 5 (bez 5) z krokiem 0.5
print(np.linspace(1,6,6),"\n")           # ciag arytmetyczny liczb z przedzialu od 1 do 6 o dlugosci 6
print(np.eye(3),"\n")                    # macierz jednostkowa  
print(np.eye(3,dtype = np.bool_),"\n")   # jak wyzej ale z okreslonym typem elementow
print(np.diag([1,7,9]),"\n")             # macierz diagonalna
print(np.zeros((4,5)),"\n")              # macierz zerowa
print(np.ones((5,5)),"\n")               # macierz wypelniona jedynkami

print("***************************************************************************************************\n")

# Macierze o elementach bedacych liczbami pseudolosowymi

print(np.random.rand(3,4),"\n")          # rozklad jednostajny na przedziale od 0 do 1
print(np.random.randn(3,4),"\n")         # rozklad normalny standardowy

# Powtarzanie wartosci

print(np.repeat("a",5),"\n")             # powtarza 5 razy napis "a"
print(np.repeat([1,2,1],4),"\n")
print(np.repeat([1,2,3],(2,3,4)),"\n")
print(np.repeat([[1,2],[3,4]],(4,5),axis = 1),"\n")    # axis = 1 - kolumna
print(np.repeat([[1,2],[3,4]],(4,5),axis = 0),"\n")    # axis = 0 - wiersz
print(np.tile("a",5),"\n")

print("***************************************************************************************************\n")

# Operacje na tablicach

print(np.append(np.array([1,2,2]),0.4),"\n")       # dodanie elementu do tablicy, wynik zawsze w postaci wektora

L = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(np.append(L,np.tile(0.5,(3,1)),axis = 1),"\n")   # nowa kolumna
print(np.append(L,np.tile(0.5,(1,3)),axis = 0),"\n")   # nowy wiersz
print(np.concatenate((A,L),axis=0),"\n")               # laczenie macierzy
print(np.row_stack((L,[1,2,3])),"\n")
print(np.column_stack((L,[1,2,3])),"\n")

print(np.insert(L,[1],[9],axis = 1),"\n")             # po pierwszej kolumnie wstawia kolumne 9
print(np.insert(L,[1],[9],axis = 0),"\n")             # po pierwszym wierszu wstawia wiersz 9

# Obiekt r_

print(np.r_[1,1,4],"\n")
print(np.r_[1,[1]*5,4],"\n")
print(np.r_[1:4],"\n")
print(np.r_[1:4:0.5],"\n")

print("***************************************************************************************************\n")

# Operatory - działania zwektoryzowane
# A + B - dodawanie
# A - B - odejmowanie
# A * B - mnozenie
# A / B - dzielenie
# A ** B -  potegowanie
# A // B - dzielenie calkowite
# A % B - reszta z dzielenia
# - A - zmiana znaku

n = np.array(np.arange(0,10,1))
s = np.array(np.arange(0,20,2))
print(n,"\n")
print(s,"\n")
print(n+s,"\n")
print(n*s,"\n")
print(0*n,"\n")
print(n+100,"\n")
print(n-s,"\n")
print(n**2,"\n")

print("***************************************************************************************************\n")

# Uwaga: Algebraiczne mnozenie macierzy - funkcja dot()

M = np.array([[1,2,3],[4,5,5],[1,0,9]])
print(M,"\n")
print(M.T,"\n")               # transpozycja macierzy M czyli zamiana kolumn na wiersze

print(np.dot(M,M.T),"\n")

# Skumulowana suma i roznica elementow tablicy

print(np.cumsum(s),"\n") # w przypadku macierzy axis = 0 dla wiersza i axis = 1 dla kolumny
print(np.diff(s),"\n")






































