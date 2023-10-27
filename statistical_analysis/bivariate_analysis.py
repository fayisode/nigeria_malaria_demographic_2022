import copy
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import chi2_contingency

def bi_variate_analysis(data, col, target):
    print('Bi variate Analysis of X = ', col, 'and Y = ', target)
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

def create_contingency_table(data, col, target):
    #Return chi valie, p-value to p and degree of freedom
    print('Column name is ', col)
    _cross_tab = pd.crosstab(data[col], data[target], margins=True, margins_name='subtotal')
    stat, p, dof, expected = chi2_contingency(_cross_tab)
    # interpret p-value
    alpha = 0.05
    print("p value is " + str(p))
    if p <= alpha:
        print('Dependent (reject H0)')
    else:
        print('Independent (H0 holds true)')
    print({
        "stat": stat,
        "p_value": p,
        "dof":dof,
    })
    print('\n\n\n')
    return _cross_tab, stat, p, dof, expected
