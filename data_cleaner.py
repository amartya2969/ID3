import csv
import math
import pandas as pd
import numpy as np
from pprint import pprint
for i in range(1,57):
    s=str(i)+".csv"
    s1="cleaned"+str(i)+'.csv'
    df1=pd.read_csv(s,header=None,index_col = False)
    df_norm = (df1 - df1.min()) / (df1.max() - df1.min())
    for j in range(0,df1.shape[0]):
        df_norm.iloc[j,20]=df1.iloc[j,20]
    df_norm.to_csv(s1, encoding='utf-8', index=False, header=False)
