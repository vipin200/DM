import pandas as pd
import numpy as np

arr = pd.read_csv("people.txt" , delimiter="\t")
print(arr.head())

brr = arr['age'].isin(range(0,150))
# brr = np.where(np.logical_and(arr['age'] <150, arr['age'] >0))
print(brr)

crr = arr['age'] > arr['yearsmarried']
print(crr)

