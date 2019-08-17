import numpy as np

ai = int(input("Określ liczbę wierszy dla macierzy A :\n"))
aj = int(input("Określ liczbę kolumn dla macierzy A :\n"))
bi = int(input("Określ liczbę wierszy dla macierzy B : \n"))
bj = int(input("Określ liczbę kolumn dla macierzy B : \n"))

if aj != bi:
    print("iloczyn A·B niemozliwy, poniewaz ilosc kolumn macierzy A jest inna niz ilosc wierszy macierzy B")
    pass

else:
    A = np.array(np.random.rand(ai, aj))
    B = np.array(np.random.rand(bi, bj))
    C = np.zeros((ai, bj))

    for i in range(len(A)):
       for j in range(len(B[0])):
           for k in range(len(B)):
               C[i][j] += A[i][k] * B[k][j]

    for r in C:
       print(r)


    print('Algebraiczne mnozenie macierzy za pomoca funkcji dot() / Numpy')
    print(A.dot(B))
    print('Algebraiczne mnozenie macierzy za pomoca symbolu @')
    print(A @ B)
