import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web

df = pd.read_excel('T_bill_2019_2020_Daily.xlsx',index_col=0) 

df_Weekly  = df.resample('W-FRI').ffill().apply(lambda x: x*365/52).shift(-1)
df_Monthly = df.resample('M').ffill().apply(lambda x: x*365/12)

df_Weekly.ix[-2,'T-Bill Return% (Daily)']=0.0825
df_Weekly.drop(df_Weekly.tail(1).index,inplace=True) 
df_Weekly.drop(df_Weekly.head(1).index,inplace=True) 
df_Monthly.drop(df_Monthly.head(1).index,inplace=True) 
                                #cleaning part which exceeds time period or is NaN i.e first and last row

df_Weekly.columns=['Weekly']
df_Monthly.columns=['Monthly'] 
                                #changing column names     

nestle_Near = pd.read_excel('Futures Near Month.xlsx',index_col=0)
                                #reading relevant excel files

nestle_Near=nestle_Near.drop_duplicates()
                                #removing duplicate rows (cleaning data to make resampling feasible)

nestle_Near['Daily Return'] = nestle_Near['Settle Price'].pct_change(1)
nestle_Near_Weekly  = nestle_Near['Settle Price'].resample('W-FRI').ffill().pct_change()   
nestle_Near_Monthly = nestle_Near['Settle Price'].resample('M').ffill().pct_change()    
                             


nestle_Near_Weekly.drop(nestle_Near_Weekly.tail(3).index,inplace=True) 
                                #cleaning data to ensure it works with weekly t-bill dataframe   

nestle_Near_Monthly.drop(nestle_Near_Monthly.head(1).index,inplace=True) 
nestle_Near_Monthly.drop(nestle_Near_Monthly.tail(1).index,inplace=True) 
                                #matching indices

df['index1'] = df.index
nestle_Near['index1']=nestle_Near.index
days = pd.merge_ordered(nestle_Near, df,on='index1', fill_method='ffill')
days['Daily Return']=days['Daily Return']*100
days['Daily Excess']=days['Daily Return']-days['T-Bill Return% (Daily)']
                                 #cleaning data & forward filling to ensure it works with daily t-bill dataframe   

weeks=pd.DataFrame(columns=['Weekly Returns','Weekly TBill','Weekly Excess'])
weeks['Weekly Returns']=nestle_Near_Weekly*100
weeks['Weekly TBill']=df_Weekly['Weekly']
weeks['Weekly Excess']=weeks['Weekly Returns']-weeks['Weekly TBill']


months=pd.DataFrame(columns=['Monthly Returns','Monthly TBill','Monthly Excess'])
months['Monthly Returns']=nestle_Near_Monthly*100
months['Monthly TBill']=df_Monthly['Monthly']
months['Monthly Excess']=months['Monthly Returns']-months['Monthly TBill']

days['Daily Excess'].plot(kind='line',title='Line Graph for Daily Excess Returns')
plt.show()


weeks['Weekly Excess'].plot(kind='line',title='Line Graph for Weekly Excess Returns')
plt.show()

months['Monthly Excess'].plot(kind='line',title='Line Graph for Monthly Excess Returns')
plt.show()
