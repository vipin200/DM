import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pr2_rules as dir
pd.set_option('display.max_rows',157)

dataset = pd.read_csv("dirty_iris.csv")

a = dir.check_species(dataset)
b = dir.check_validity(dataset)
c = dir.check_petal_length_width(dataset)
d = dir.check_sepal_length(dataset)
e = dir.check_sepal_petal(dataset)

n = len(a)
temp = [True] * len(a)
for i in range(4):
    temp = temp & b.iloc[:,i]

b = temp

r1 = a.value_counts()
r2 = b.value_counts()
r3 = c.value_counts()
r4 = d.value_counts()
r5 = e.value_counts()

breaks_rule = a & b & c & d & e
b_r = breaks_rule.value_counts()

# print("\n\nRule 1 :– Species should be one of the following values: setosa, versicolor or virginica.\n\t  Followed by : \t{}\n\t  Not followed by :\t{} \n\nRule 2 :– All measured numerical properties of an iris should be positive.\n\t  Followed by : \t{}\n\t  Not followed by :\t{} \n\nRule 3 :– The petal length of an iris is at least 2 times its petal width.\n\t  Followed by : \t{}\n\t  Not followed by :\t{} \n \nRule 4 :– The sepal length of an iris cannot exceed 30 cm.\n\t  Followed by : \t{}\n\t  Not followed by :\t{} \n\nRule 5 :– The sepals of an iris are longer than its petals.\n\t  Followed by : \t{}\n\t  Not followed by :\t{} \n".format(r1[1],n-r1[1],r2[1],n-r2[1],r3[1],n-r3[1],r4[1],n-r4[1],r5[1],n-r5[1]))

# print("\nObservations that violates atleast one rule : \t{}\nObservations that does not violates any rule : \t{}".format(b_r[1],n-b_r[1]))

labels = ['R1', 'R2', 'R3', 'R4', 'R5', 'R1-R5']
X = [r1[1],r2[1],r3[1],r4[1],r5[1],b_r[1]]
Y = [n-r1[1],n-r2[1],n-r3[1],n-r4[1],n-r5[1],n-b_r[1]]


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, X, width, label='Follow Rules')
rects2 = ax.bar(x + width/2, Y, width, label='Don\'t Follow Rules')

ax.set_ylabel('Observations')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

dataset = dataset.replace([np.inf, -np.inf], np.nan)
dataset[dataset.iloc[:,:4]<0] = np.nan

n = len(dataset)
n1 = len(dataset.dropna())

print('\nNumber of total observations:          {}\nNumber of complete observations:        {}'.format(n,n1))
print('\nPercentage of complete observations:    {}%'.format(int((n1/n)*100)))

plt.show()

# ax.set_title('Basic Plot')
# ax.boxplot(dataset.iloc[:,0:4])

# plt.show()