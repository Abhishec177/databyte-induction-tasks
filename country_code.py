import csv
import pandas as pd

df = pd.read_csv('data_csv.csv')
df = df.sort_values('Name',ascending=True)
##df[['Name','Code']]
##df.iloc[1][1]

res = []
for i in range(0,249):
    country = { i:df.iloc[i][1],df.iloc[i][1]: df.iloc[i][0]}
    res.append(country)
    
#res

def display(a,b):
    flag = 0
    for i,code in enumerate(res):
        if(code[i]==a):
            flag = 1
        if(code[i]==b):
            flag = 0
        if(flag ==1 and code[i]!=a):
            print(code[code[i]])

a  = str(input())
b = str(input())            
display(a,b)
