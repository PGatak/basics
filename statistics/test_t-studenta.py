# -*- coding: utf-8 -*-

import math
import random
from scipy import stats


dane_1 = [random.randint(a,b) for a in range(0,50) for b in range(60,100)]

dane_2 = [random.randint(a,b) for a in range(0,50) for b in range(60,100)]

# Tesst t-studenta dla jednej próby:

test_1 = stats.ttest_1samp(dane_1,52)

# Tesst t-studenta dla dwóch prób niezależnych:

test_2 = stats.ttest_ind(dane_1,dane_2)             

# Tesst t-studenta dla dwóch prób niezależnych (ze statystyk opisowych):

test_3 = stats.ttest_ind_from_stats(mean1=10.0, std1=math.sqrt(88.5), nobs1=20,mean2=15.0, std2=math.sqrt(70.0), nobs2=13)

# Test t-studenta dla dwóch prób zależnych:

test_4 = stats.ttest_rel(dane_1,dane_2)

# Test Bartletta równoci wariancji próbek o rozkładzie normalnym:

test_5 = stats.bartlett(dane_1, dane_2)

# Test Levene'a równoci wariancji:

test_6 = stats.levene(dane_1, dane_2)

# Test Mood's równoci median:

test_7 = stats.median_test(dane_1, dane_2)

