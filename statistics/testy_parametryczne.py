# -*- coding: utf-8 -*-

import math
import random
from scipy import stats


# Test t-studenta dla jednej próby:

stats.ttest_1samp(dane_1,52)

# Test t-studenta dla dwóch prób niezależnych:

stats.ttest_ind(dane_1,dane_2)             

# Test t-studenta dla dwóch prób niezależnych (ze statystyk opisowych):

stats.ttest_ind_from_stats(mean1=10.0, std1=math.sqrt(88.5), nobs1=20,mean2=15.0, std2=math.sqrt(70.0), nobs2=13)

# Test t-studenta dla dwóch prób zależnych:

stats.ttest_rel(dane_1,dane_2)

# Test Bartletta równoci wariancji próbek o rozkładzie normalnym:

stats.bartlett(dane_1, dane_2)

# Test Levene'a równoci wariancji:

stats.levene(dane_1, dane_2)

# Test Mood's równoci median:

stats.median_test(dane_1, dane_2)

# Jednoczynnikowa ANOVA (dla prób niezależnych):

stats.f_oneway(dane_1, dane_2, dane_3)

