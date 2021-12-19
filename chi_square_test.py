import numpy as np
import pandas as pd
from scipy.stats.contingency import chi2_contingency

# create a row list for chi square test 
def row_list(data):
    data=pd.read_csv(data)
    row =[]
    count =0
    for index,rows in data.iterrows():
        my_list = [rows.pizza, rows.burger, rows.fruit]
        row.append(my_list)
        count=count+1
    print(count)
    return row 

# perform the chi-square test 
def suman(data):
    data = row_list(data)
    stat, p, dof, expected=chi2_contingency(data)
    alpha=0.5
    if(p<=alpha):
        print("null hypothesis is TRUE")
    else:
        print("alternate hypothesis is true !")
    


file = 'book1.csv'

print(suman(file))
print(row_list(file))
