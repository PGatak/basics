# -*- coding: utf-8 -*-

import math
import random
from scipy import stats


# Test Mood's równoci median:

stats.median_test(dane_1, dane_2)

# Test U Manna Whitney'a (nieparametryczny odpowiednik testu t-studenta dla prób niezależnych):

stats.mannwhitneyu(dane_1, dane_2)

# Test Wilcoxsona (odpowiednik testu t-studenta dla prób zależnych):

stats.wilcoxon(dane_1, dane_2)

# Test Kurskala - Wallisa (nieparametryczny odpowiednik jednoczynnikowej ANOVA dla prób niezależnych):

stats.kruskal(dane_1, dane_2, dane_3)

# Test Friedmana (nieparametryczny odpowiednik jednoczynnikowej ANOVA dla prób zależnych):

stats.friedmanchisquare(dane_1, dane_2, dane_3)
















