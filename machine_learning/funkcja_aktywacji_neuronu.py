import matplotlib.pyplot as plt
import math
import numpy as np


plt.rcParams['xtick.labelsize'] = 7
plt.rcParams['ytick.labelsize'] = 7


#z = [i for i in range(-10, 11)]
z = np.arange(- 10, 10, 0.1)


def progowa_unipolarna(lst):
    lst.sort()
    results = []
    for i in lst:
        if i > 0:
            result = 1
        else:
            result = 0
        results.append(result)
    return results


def progowa_bipolarna(lst):
    lst.sort()
    results = []
    for i in lst:
        if i > 0:
            result = 1
        else:
            result = -1
        results.append(result)
    return results


def sigmoidalna_unipolarna(lst):
    lst.sort()
    results = []
    for i in lst:
        result = 1 / (1 + math.e ** (0.5 * - i))
        results.append(result)
    return results


def tangens_hiperboliczny(lst):
    lst.sort()
    results = []
    for i in lst:
        result = math.tanh((0.5 * i) / math.e)
        # lub result = (1 - math.e ** (0.5 * - i)) / (1 + math.e ** (0.5 * - i))
        results.append(result)
    return results

fig = plt.figure()
plt.subplot(2, 2, 1)
plt.plot(z, progowa_unipolarna(z))
plt.title("Progowa unipolarna")

plt.subplot(2, 2, 2)
plt.plot(z, progowa_bipolarna(z))
plt.plot(z, 0 * z)
plt.title("Progowa bipolarna")

plt.subplot(2, 2, 3)
plt.plot(z, sigmoidalna_unipolarna(z))
plt.title("Sigmoidalna unipolarna, β = 0.5")

plt.subplot(2, 2, 4)
plt.plot(z, tangens_hiperboliczny(z))
plt.plot(z, 0 * z)
plt.title("Tangens hiperboliczny, α = 0.5")
plt.tight_layout()
plt.show()
fig.savefig('neuron_activation_function.jpg')