import pandas as pd

def Current(x):
    if x >= 1000:
        return 0
    else:
        return x

def Time(x):
    if x >=500:
        return 0
    else:
        return x
x=pd.read_csv("F:/Data/R/Test/RStudio/vid2.csv")
c=x.columns

x1=x[x.iloc[:,3]==3] #筛选充电状态
x1=x1[x1.iloc[:,2]!=3] #去除其他状态
x2=x1.copy()
x2.iloc[:,1]=pd.to_datetime(x2.iloc[:,1], format='%Y%m%d%H%M%S')
x2=x2.sort_values(by=c[1])
x3=x2.copy()
x3.iloc[:,8]=x2.iloc[:,8].apply(lambda x: Current(x))
x3['Charge_Time']=0
#x2=x2.drop('Charge_Time',axis=1) 丢弃

for i in range(0,len(x2)-2):
    x3.iloc[i,17]=(x2.iloc[i+1,1]-x2.iloc[i,1]).seconds
x4=x3.copy()
x4.iloc[:,17]=x3.iloc[:,17].apply(lambda x: Time(x))
x5=x4.copy()
x5['Charge_current']=0
for i in range(0,len(x4)-2):
    x5.iloc[i,18]=(x4.iloc[i+1,8]+x4.iloc[i,8])/2
# x4['Charge_Time'][x3.Charge_Time>500]=0 另一种按条件赋值
x5['dQ']=0
x6=x5.copy()
for i in range(0,len(x5)-2):
    x6.iloc[i,19]=x5.iloc[i,18]*x5.iloc[i,17]
x6.to_csv('Charge_vid2.csv')