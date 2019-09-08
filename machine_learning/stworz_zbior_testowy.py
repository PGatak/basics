import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.DataFrame(np.linspace(0, 10, 20).reshape(10, 2))


# 1
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


train_set, test_set = split_train_test(df, 0.2)
print("Uczące", len(train_set), ", testowe", len(test_set))


# 2
train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
print("Uczące", len(train_set), ", testowe", len(test_set))
