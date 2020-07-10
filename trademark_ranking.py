import os
import numpy as np
import pandas as pd
import io
from pandas import DataFrame

df =  pd.read_csv("result.txt",sep='\t',header=0)
# print(df.head())

df = df.dropna(subset=['trademark'])
sum = dict(df.loc[:,'trademark'].value_counts())
# print(type(sum))
sum_value = sorted(sum.items(), key=lambda item:item[1], reverse=True)
# print(sum_value[0:4999])

x_list = [x[0] for x in sum_value[0:4999]]
# print(x_list)

res_df = df[df.trademark.isin(x_list)]

# results = res.groupby('trademark').size()
print(res_df)
res_df.to_csv('results.txt',sep='\t', index=False)



