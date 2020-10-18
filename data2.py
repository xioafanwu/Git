import numpy as np
import pandas as pd
import missingno as msno

x=pd.read_csv("F:/Data/R/Test/RStudio/vid1.csv")
n=len(x)

k=0
x1=x.iloc[:,1]
result = pd.value_counts(x1)
msno.matrix(x, labels=True)
'''
for i in range(1,n):
    if x['status'][i]==3 and x['c_stat'][i]==3 and x['mode'][i]==1:
        x1=x.drop([i])
        k+=1
'''
# print(result)