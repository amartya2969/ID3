import csv
import math
import pandas as pd
import numpy as np
from pprint import pprint
arr=[]
for i in range(1,57):
    s=str(i)+'.csv'
    df1=pd.read_csv(s,header=None)
    def parent_entropy():
        c=0
        for i in range(df1.shape[0]):
            if df1.iloc[i,20]==0:
                c=c+1
        if c==0:
            return 0

        pentropy=-((c/df1.shape[0]*math.log2(c/df1.shape[0]))+(((df1.shape[0]-c)/df1.shape[0]*math.log2((df1.shape[0]-c)/df1.shape[0]))))
        return pentropy
    def entropy_children(column_name,avg):
        c=0
        c1=0
        for i in range(df1.shape[0]):
            if df1.iloc[i,column_name]<avg:
                c=c+1
                if df1.iloc[i,20]==0:
                    c1=c1+1
        t1=0
        if c1 !=0:
            if (c-c1) !=0:
                t1=-((c1/c*math.log2(c1/c))+(((c-c1)/c)*math.log2((c-c1)/c)))
        d=0
        d1=0
        for i in range(df1.shape[0]):
            if df1.iloc[i,column_name]>=avg:
                d=d+1
                if df1.iloc[i,20]==0:
                    d1=d1+1
        t2=0
        if d1 !=0:
            if (d-d1)!=0:
                t2=-((d1/d*math.log2(d1/d))+(((d-d1)/d)*math.log2((d-d1)/d)))
        s=((c/df1.shape[0])*t1)+((d/df1.shape[0])*t2)
        return s
    def info_gain():
        ls=[]
        for i in range(0,19):
            average=df1.iloc[:,i].mean()
            parent1=parent_entropy()
            child1=entropy_children(i,average)
            answer=parent1-child1
            ls.append(answer)
        arr.append(ls)
        return answer
    info_gain()
with open("data1.csv", mode='w') as csvFile:
    writer = csv.writer(csvFile)
    for row in arr:
        writer.writerow(row)
