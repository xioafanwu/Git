# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:24:45 2019

@author: liang
"""



import pandas as pd
import numpy as np


#预测结果读取
file_submit = open('G:/self/py/energy-submit.csv')
submit = pd.read_csv(file_submit)

#真实结果读取
file_result = open('G:/self/py./energy-result.csv')
result = pd.read_csv(file_result)

#评分
error = (result['charge_energy'] - submit['charge_energy'])/result['charge_energy']
score = (np.mean(error**2))**0.5
print(score)