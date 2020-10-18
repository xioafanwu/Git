import numpy as np
import pandas as pd
from dateutil.parser import parse
x=pd.read_csv('F:/Data/R/Test/RStudio/vid8.csv')
x['db74f2ad.fa76.480a.8951.d1bca1e021ff.daq_time']=pd.to_datetime(x['db74f2ad.fa76.480a.8951.d1bca1e021ff.daq_time'], format='%Y%m%d%H%M%S') 
x1=x.iloc[:,1]
n=len(x1)
y1=np.zeros(n)
for i in range(1,n):
    y1[i]=(x1[i+1]-x1[i]).seconds
result = pd.value_counts(y1)
result.to_excel('vid8_result.xlsx')
np.savetxt("vid8_time.csv", y1, delimiter=',')