import pandas as pd
import numpy as np
data =  pd.read_csv("dirty_iris.csv")
data = data.replace([np.inf,-np.inf] , np.nan )
complete = len(data.dropna())
total = len(data)
print("Percentage of observations that are complete: ",end="")
print(complete/total * 100)


def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')


data = data._get_numeric_data()

# data[data < 0] = np.nan
# print_full(data)
data.describe()