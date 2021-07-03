import numpy as np
import random
import pandas as pd
from sklearn.linear_model import LinearRegression

def hampel(vals_orig):
    vals = vals_orig.copy()
    difference = np.abs(vals.median() - vals)
    median_abs_deviation = difference.median()
    threshold = 2 * median_abs_deviation
    outlier_idx = difference > threshold
    vals[outlier_idx] = np.nan
    return vals

data = pd.read_csv('ClothingStore.csv')
print(f"До\n")
print(f"Среднее значение (медиана)\n{data.median()}")
print(f"Максимальное значение\n{data.max()}")
print(f"Минимальное значение\n{data.min()}")
"разница с медианой больше, чем два медианных абсолютных отклонения"
print(f"После применения фильтра Хэмпеля\n")
table = dict()
for i in range(4):
    table[i] = hampel(data.iloc[:, i])
dataFrame = pd.DataFrame(data=table)
dataFrame.columns = ["Headdress", "Outerwear", "Trousers ", "Footwear"]
print(f"После устранения пропусков\n")
for i in range(4):
    med = dataFrame.iloc[:, i].median()
    dataFrame.iloc[:, i] = dataFrame.iloc[:, i].fillna(med)
print(f"Среднее значение (медиана)\n{dataFrame.median()}")
print(f"Максимальное значение\n{dataFrame.max()}")
print(f"Минимальное значение\n{dataFrame.min()}")
dataFrame.to_csv("newClothingStore.csv", index=False)