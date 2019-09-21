import matplotlib.pyplot as plt
import math

z = [i for i in range(-10, 11)]


def logistic_regression(lst):
    lst.sort()
    results = []
    for i in lst:
        result = 1 / (1 + math.e ** (- i))
        results.append(result)
    return results


plt.plot(z, logistic_regression(z))
plt.show()
