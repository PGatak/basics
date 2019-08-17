import numpy

M = [[-5, 2, 1], [4, 2, 3], [2, 1, 0]]

print(round(numpy.linalg.det(M), 5))

print("Oblicz macierz stopnia n=1")
a11 = float(input("Podaj a11\n"))

det = a11
print("wyznacznik macierzy wynosi", det)


print("Oblicz macierz stopnia n=2")
a11 = float(input("Podaj a11\n"))
a12 = float(input("Podaj a12\n"))
a21 = float(input("Podaj a21\n"))
a22 = float(input("Podaj a22\n"))

det = a11 * a22 - a12 * a21
print("wyznacznik macierzy wynosi", det)


print("Oblicz macierz stopnia n=3")
a11 = float(input("Podaj a11\n"))
a12 = float(input("Podaj a12\n"))
a13 = float(input("Podaj a13\n"))
a21 = float(input("Podaj a21\n"))
a22 = float(input("Podaj a22\n"))
a23 = float(input("Podaj a23\n"))
a31 = float(input("Podaj a21\n"))
a32 = float(input("Podaj a22\n"))
a33 = float(input("Podaj a23\n"))

det = (a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32) - (a13 * a22 * a31) - (a11 * a23 * a32) - (a12 *a21 * a33)
print("wyznacznik macierzy wynosi", det)
