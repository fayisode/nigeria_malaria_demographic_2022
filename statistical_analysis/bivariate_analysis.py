import copy
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def bi_variate_analysis(data, col, target):
    print('Bi variate Analysis of X = ', col, 'Y = ', target)
    _type = data[col].dtypes
    print('Column data type is', _type)
    _data = copy.deepcopy(data)
    if data[col].dtypes == 'object':
        pivot_table = data.pivot_table(index=target, columns=col, aggfunc='size')
        sns.heatmap(pivot_table, annot=True)
        plt.show()
        print(pd.crosstab(_data[col], _data[target]))
        sns.heatmap(pd.crosstab(_data[col], _data[target]))
        plt.show()
    else:
        sns.boxplot(x=col, y=target, data=_data)
        plt.show()
        sns.barplot(x=col, y=target, data=_data)
        plt.show()
        sns.stripplot(x=col, y=target, data=_data)
        plt.show()
        sns.scatterplot(x=col, y=target, data=_data)
        plt.show()
