import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web

df = pd.read_excel('Futures Next Month.xlsx',index_col=0) 

df=df.drop_duplicates()
df['Daily Return'] = df['Settle Price'].pct_change(1)
df['Daily Return']=df['Daily Return']*100
df_Weekly  = df['Settle Price'].resample('W-FRI').ffill().pct_change()   
df_Weekly  =df_Weekly  *100
df_Monthly = df['Settle Price'].resample('M').ffill().pct_change()   
df_Monthly =df_Monthly *100

print("Daily Returns")
print("Maximum:"+ str(round(df['Daily Return'].max(axis=0),3)))    
print("Minimum:"+str(round(df['Daily Return'].min(axis=0),3)))  
print("Mean:"+str(round(df['Daily Return'].mean(),4)))  
print("Sample Standard Deviation:"+str(round(df['Daily Return'].std(axis=0),4)))  


print("Weekly Returns")
print("Maximum:"+ str(round(df_Weekly.max(axis=0),3)))    
print("Minimum:"+str(round(df_Weekly.min(axis=0),3)))  
print("Mean:"+str(round(df_Weekly.mean(),4)))  
print("Sample Standard Deviation:"+str(round(df_Weekly.std(axis=0),4)))  


print("Monthly Returns")
print("Maximum:"+ str(round(df_Monthly.max(axis=0),3)))    
print("Minimum:"+str(round(df_Monthly.min(axis=0),3)))  
print("Mean:"+str(round(df_Monthly.mean(),4)))  
print("Sample Standard Deviation:"+str(round(df_Monthly.std(axis=0),4)))  


df['Daily Return'].plot(kind='line',title='Line Graph for Unadjusted Daily Returns of Next Month')
plt.show()
df_Weekly.plot(kind='line',title='Line Graph for Unadjusted Weekly Returns of Next Month')
plt.show()
df_Monthly.plot(kind='line',title='Line Graph for Unadjusted Monthly Returns of Next Month')
plt.show()


