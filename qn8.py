import pandas as pd
df=pd.read_csv("filename.csv")
#imagine csv file contains name,maths,eng,comp as columns and they contain missing values
avg=df[['maths','eng','comp']].mean()
fulldf=df.fillna(avg)#complete with filled missing values
print(fulldf)
subavg=df[['maths','eng','comp']].mean()
print(subavg)#this prints averages for each subjects
