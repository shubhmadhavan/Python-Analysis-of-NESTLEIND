import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web


df = web.get_data_yahoo("NESTLEIND.NS",
                            start = "2019-04-01",
                            end = "2020-03-31")        
                             #adds reproducability of code and flexibility of time period    

"""We can also use the following code in comments if the scraped csv from attached zip is used

df = pd.read_csv('NESTLEIND.csv',header=[0])            """

df['Daily_Return']=df['Close'].pct_change()
                                #Daily Returns have been stored in a separate column
df['Daily_Return']=df['Daily_Return']*100                                
                                #will be relevant as we need to return values in% and not /100 

print("Daily Returns %")
print("Maximum:"+ str(round(df['Daily_Return'].max(axis=0),3)))    
print("Minimum:"+str(round(df['Daily_Return'].min(axis=0),3)))  
print("Mean:"+str(round(df['Daily_Return'].mean(),4)))  
print("Sample Standard Deviation:"+str(round(df['Daily_Return'].std(axis=0),4)))  

df['Daily_Return'].plot(kind='line',title='Line Graph for Daily Returns')
plt.show()

print(df['Daily_Return'])

