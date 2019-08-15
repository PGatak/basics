from scipy import stats
from preparation import data_1, data_2

test_1 = stats.levene(data_1.PRZED_1, data_1.PO_1)
print(test_1)
test_2 = stats.ttest_rel(data_1.PRZED_1, data_1.PO_1)
print(test_2)

test_3 = stats.levene(data_2.PRZED_2, data_2.PO_2)
print(test_3)
test_4 = stats.ttest_rel(data_2.PRZED_2, data_2.PO_2)
print(test_4)

# test_3 = stats.levene(data_2.PO_2, data_1.PO_1)
# print(test_3)
# test_4 = stats.ttest_ind(data_2.PO_2, data_1.PO_1)
# print(test_4)
#
# test_3 = stats.levene(data_2.PRZED_2, data_1.PRZED_1)
# print(test_3)
# test_4 = stats.ttest_ind(data_2.PRZED_2, data_1.PRZED_1)
# print(test_4)