import pandas as pd
import re
import numpy as np
from fuzzywuzzy import fuzz
import copy

#Use fuzzy logic for simplicity
#Print functions used to visualize merging events
df=copy.copy(test_data)
#print(df)
def column_merge(df,thresh=None,start_point=0):
    """
    Add columns together based on similarity of column names

    Parameters
    ----------
    df : pandas dataframe object
        A dataframe object with at least 2 columns and 1 row
    thresh : int, default=60
        Matching threshhold between 0 and 100. Listed as none to allow for update in each recursive call

    Returns
    -------
    DataFrame: with merged column name
    """
    thresh=60
    size=len(df.columns)-1

    for i in range(start_point,size):
        if i+1==len(df.columns):
            break
        elif fuzz.ratio(df.columns[i],df.columns[i+1])>thresh:
            df.iloc[:,i]+=df.iloc[:,i+1]
            #print(">>column merged at %i and %i with fuzz = %i > %i"%(i,i+1,fuzz.ratio(df.columns[i],df.columns[i+1]),thresh))
            df.drop(df.columns[i+1],axis=1,inplace=True)
            #print(df)
            column_merge(df,start_point)
        else:
            0
        start_point+=1
        #print(">>column skipped at %i and %i with fuzz = %i < %i"%(i,i+1,fuzz.ratio(df.columns[i],df.columns[i+1]),thresh))
        #print(df)

    return df