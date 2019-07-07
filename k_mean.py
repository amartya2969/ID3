import csv
import math
from sklearn.cluster import KMeans
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as pld3
from matplotlib import style
from pprint import pprint
ans=[]
ans_final=[]
for t in range(1,57):
    ls=[]
    ls1=[]
    s="cleaned"+str(t)+'.csv'
    df=pd.read_csv(s,header=None,index_col = False)
    centroid_1=[]
    centroid_2=[]
    previous_centroid1=[]
    previous_centroid2=[]
    error=.0001
    rows_to_be_classified=df.shape[0]
    arr1=[]
    silhouette1=[]
    for i in range(0,rows_to_be_classified):
        arr1.append(0)
    for i in range(0,20):
        num=df.iloc[0,i]
        centroid_1.append(num)
    for i in range(0,20):
        num=df.iloc[1,i]
        centroid_2.append(num)
    for i in range(0,20):
        previous_centroid1.append(centroid_1[i])
        previous_centroid2.append(centroid_2[i])
    def centroid_distance():
        inter_centroid_distance=0
        inter_centroid_distance1=0
        inter_centroid_distance2=0
        for i in range(0,20):
            inter_centroid_distance1=inter_centroid_distance1+(previous_centroid1[i]-centroid_1[i])*(previous_centroid1[i]-centroid_1[i])
            inter_centroid_distance2=inter_centroid_distance2+(previous_centroid2[i]-centroid_2[i])*(previous_centroid2[i]-centroid_2[i])
        dummy1=math.sqrt(inter_centroid_distance1)
        dummy2=math.sqrt(inter_centroid_distance2)
        inter_centroid_distance=min(dummy1,dummy2)
        print(inter_centroid_distance)
        if inter_centroid_distance > error:
            return True
        else:
            return False
    def distance_centroid1(i):
        ans=0
        for k in range(0,20):
            ans=ans+(centroid_1[k]-df.iloc[i,k])*(centroid_1[k]-df.iloc[i,k])
        dist1=math.sqrt(ans)
        return ans
    def distance_centroid2(i):
        ans=0
        for k in range(0,20):
            ans=ans+(centroid_2[k]-df.iloc[i,k])*(centroid_2[k]-df.iloc[i,k])
        dist1=math.sqrt(ans)
        return ans
    def new_centroid():
        count_cluster_1=0
        count_cluster_2=0
        for i in range(0,20):
            previous_centroid1[i]=centroid_1[i]
            previous_centroid2[i]=centroid_2[i]
        for i in range(0,20):
            centroid_1[i]=0
            centroid_2[i]=0
        for i in range(0,rows_to_be_classified):
            if arr1[i] == 1:
                count_cluster_1=count_cluster_1+1
                for j in range(0,20):
                    centroid_1[j]=centroid_1[j]+df.iloc[i,j]
            else:
                count_cluster_2=count_cluster_2+1
                for j in range(0,20):
                    centroid_2[j]=centroid_2[j]+df.iloc[i,j]
        for i in range(0,20):
            if count_cluster_1!=0:
                centroid_1[i]=centroid_1[i]/count_cluster_1
            if count_cluster_2 !=0:
                centroid_2[i]=centroid_2[i]/count_cluster_2
    def next_iteration():
        distance_from_centroid1=[]
        distance_from_centroid2=[]
        for i in range(0,rows_to_be_classified):
            dist1=distance_centroid1(i)
            dist2=distance_centroid2(i)

            if dist1>dist2:
                arr1[i]=2
            else:
                arr1[i]=1
        new_centroid()
    def sum_of_squared_errors():
        sse=0
        for i in range(0,rows_to_be_classified):
            if arr1[i]==1:
                temp1=distance_centroid1(i)
                # print(temp1)
                sse=sse+temp1*temp1
            else:
                temp2=distance_centroid2(i)
                # print(temp2)
                sse=sse+temp2*temp2
        return sse
    def distance(i,j):
        ans=0
        for k in range(0,20):
            temp1=df.iloc[i,k]-df.iloc[j,k]
            ans=ans+temp1*temp1
        return math.sqrt(ans)
    def silhouette():
        average_silhouette=0
        for i in range(0,rows_to_be_classified):
            a=0
            b=1000000
            for j in range(0,rows_to_be_classified):
                if arr1[i]==arr1[j]:
                    a=a+distance(i,j)
            a=a/rows_to_be_classified
            for j in range(0,rows_to_be_classified):
                if arr1[i]!=arr1[j]:
                    b=min(b,distance(i,j))
            silhouette1.append((b-a)/max(a,b))
            average_silhouette=average_silhouette+(b-a)/max(a,b)
        average_silhouette=average_silhouette/rows_to_be_classified
        return average_silhouette
    for i in range(0,100):
        next_iteration()
        print(i)
        val1=centroid_distance()
        if val1==False:
            break
    ls.append(centroid_1)
    ls.append(centroid_2)
    sumOfSquared=sum_of_squared_errors()
    silVal=silhouette()
    ls1.append(sumOfSquared)
    ls1.append(silVal)
    ans.append(ls)
    ans_final.append(ls1)
with open("centroid_data.csv", mode='w') as csvFile:
    writer = csv.writer(csvFile)
    for row in ans:
        writer.writerow(row)
with open("SSE_Silhouette.csv", mode='w') as csvFile:
    writer = csv.writer(csvFile)
    for row in ans_final:
        writer.writerow(row)
