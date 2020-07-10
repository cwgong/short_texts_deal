import os
import numpy as np
import pandas as pd
import io
from pandas import DataFrame

df =  pd.read_csv("dp_brands.txt",sep='\x01',header=None,names=['shop_id','shop_name'])
print(df.head())
#import pkuseg                                                                   

#pku_seg = pkuseg.pkuseg(postag=True)                                            
#pku_results = pku_seg.cut('简爱鲜花(木兮花店)')    
#print(pku_results)
shop_id=df['shop_id'].tolist()
shop_name=df['shop_name'].tolist()
trademark={}
_id=[]
_name=[]
_tid=[i for i in range(len(shop_id))]
_sid=[]
with io.open('trademark.txt',"r",encoding="utf-8") as file:
    text = file.read()
    paragraphs = text.split("\n")
    print(len(paragraphs))
    for i in range(len(paragraphs)):
        paragraph=paragraphs[i]
        if paragraph:
            values=paragraph.split('\t')
            tmpid=int(values[0])
            mark=values[1]
            _sid.append(tmpid)
            trademark[tmpid]=mark
list3=list(set(_tid).difference(set(_sid))) 
if list3:
    for t in list3:
        trademark[t]=''


trademark1=list(trademark.values())
dataInfo={}
dataInfo['shop_id']=shop_id
dataInfo['shop_name']=shop_name
dataInfo['trademark']=trademark1
df=DataFrame(dataInfo)  
df.to_csv('result.csv',index=0)
df.to_csv('result.txt', sep='\t', index=False)
