# coding: utf-8
"""
1）数据格式：第一列：店铺编号；第二列：店铺名称
2）分割符为：lst1 = line.split("\x01")
3）最终数据结果为：top5000的品牌；数据格式为：店铺编号\t店铺名称\t品牌
注：top5000指的是品牌出现的次数的top5000的品牌

4）例子：
       店名: 肯德基万达店    品牌: 肯德基
        店名: xxx鲜花店         品牌: xxx鲜花店
"""
#http://www.dianping.com/shop/73631753
import os
import io
import numpy as np
import pandas as pd
from pandas import DataFrame
import paddlehub as hub

df =  pd.read_csv("dp_brands.txt",sep='\x01',header=None,names=['shop_id','shop_name'])
print(df.head())
#import pkuseg                                                                   

#pku_seg = pkuseg.pkuseg(postag=True)                                            
#pku_results = pku_seg.cut('简爱鲜花(木兮花店)')    
#print(pku_results)
shop_id=df['shop_id'].tolist()
shop_name=df['shop_name'].tolist()
lac = hub.Module(name="lac")
test_text = ["雅马哈电动车(大关路店)", "ZIPPO(万达广场店)", "puma(大融城店)"]

trademark=[]
for m in range(len(shop_name)):
    try:
        results = lac.lexical_analysis(texts=[shop_name[m]], use_gpu=True, batch_size=1, return_tag=True)
    
    
        tag=results[0]['tag']
        word=results[0]['word']
        print("-"*20)
        print(m)
        print(word)
        print(tag)
        tmp=''
        if tag:
            for i in range(len(tag)):
                if tag[i] in ['ORG','nz']:
                    tmp=word[i]
                    break
    except Exception as e:
        print('error:',e)
        tmp=''
    print(tmp)
    trademark.append(tmp)
    with io.open('trademark.txt',"a",encoding="utf-8") as file:
        file.write(str(m)+'\t'+tmp+'\n')  
# dataInfo={}
# dataInfo['shop_id']=shop_id
# dataInfo['shop_name']=shop_name
# dataInfo['trademark']=trademark
# df=DataFrame(dataInfo)  
# df.to_csv('result.csv',index=0)




