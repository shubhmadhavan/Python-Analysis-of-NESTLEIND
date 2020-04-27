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

nestle = web.get_data_yahoo("NESTLEIND.NS",
                            start = "2019-04-01",
                            end = "2020-03-31")

nestle_weekly_returns = nestle['Close'].resample('W-FRI').ffill().pct_change()  
nestle_monthly_returns = nestle['Close'].resample('M').ffill().pct_change()


nestle_weekly_returns.drop(nestle_weekly_returns.tail(1).index,inplace=True) 
nestle_weekly_returns.drop(nestle_weekly_returns.head(1).index,inplace=True) 
nestle_monthly_returns.drop(nestle_monthly_returns.head(1).index,inplace=True) 
                                #cleaning data to ensure it works with weekly t-bill dataframe   





weeks=pd.DataFrame(columns=['Weekly Returns','Weekly TBill','Weekly Excess'])
weeks['Weekly Returns']=nestle_weekly_returns*100
weeks['Weekly TBill']=df_Weekly['Weekly']
weeks['Weekly Excess']=weeks['Weekly Returns']-weeks['Weekly TBill']


months=pd.DataFrame(columns=['Monthly Returns','Monthly TBill','Monthly Excess'])
months['Monthly Returns']=nestle_monthly_returns*100
months['Monthly TBill']=df_Monthly['Monthly']
months['Monthly Excess']=months['Monthly Returns']-months['Monthly TBill']



days=pd.DataFrame(columns=['Daily Returns','Daily TBill','Daily Excess'])
days['Daily_Return']=nestle['Close'].pct_change(1)
days['Daily Returns']=days['Daily_Return']*100
days['Daily TBill']=df['T-Bill Return% (Daily)']
days['Daily Excess']=days['Daily Returns']-days['Daily TBill']

print("Risk Adjusted Data:")
print("1.Daily Data:")
print("Maximum:"+ str(round(days['Daily Excess'].max(axis=0),3)))    
print("Minimum:"+str(round(days['Daily Excess'].min(axis=0),3)))  
print("Mean:"+str(round(days['Daily Excess'].mean(),3)))  
print("Sample Standard Deviation:"+str(round(days['Daily Excess'].std(axis=0),3)))  
print()
print("2.Weekly Data:")
print("Maximum:"+ str(round(weeks['Weekly Excess'].max(axis=0),3)))    
print("Minimum:"+str(round(weeks['Weekly Excess'].min(axis=0),3)))  
print("Mean:"+str(round(weeks['Weekly Excess'].mean(),3)))  
print("Sample Standard Deviation:"+str(round(weeks['Weekly Excess'].std(axis=0),3)))  
print()
print("3.Monthly Data:")
print("Maximum:"+ str(round(months['Monthly Excess'].max(axis=0),3)))    
print("Minimum:"+str(round(months['Monthly Excess'].min(axis=0),3)))  
print("Mean:"+str(round(months['Monthly Excess'].mean(),3)))  
print("Sample Standard Deviation:"+str(round(months['Monthly Excess'].std(axis=0),3)))  


"""
np_tbill_daily=df['T-Bill Return% (Daily)'].to_numpy()
np_tbill_weekly=df_Weekly.to_numpy().transpose()
np_tbill_monthly=df_Monthly.to_numpy()
                                    #creating numpy arrays for tbills
np_nestle_daily=nestle['Close'].pct_change(1).to_numpy()
np_nestle_weekly=nestle_weekly_returns.to_numpy()
np_nestle_monthly=nestle_monthly_returns.to_numpy()
                                    #creating numpy arrays for nestle returns


print(np.subtract(np_nestle_weekly,np_tbill_weekly))"""