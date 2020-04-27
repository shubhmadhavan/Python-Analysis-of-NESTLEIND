import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web


nestle = web.get_data_yahoo("NESTLEIND.NS",
                            start = "2019-04-01",
                            end = "2020-03-31")

nestle_monthly_returns = nestle['Close'].resample('M').ffill().pct_change()
                #resampling all dates on basis of month and forward filling the data
                #even if the last day of the month is a holiday, the previous day is taken and filled in that day
nestle_monthly_returns = nestle_monthly_returns *100


print("Monthly Returns")
print("Maximum:"+ str(round(nestle_monthly_returns.max(axis=0),3)))    
print("Minimum:"+str(round(nestle_monthly_returns.min(axis=0),3)))  
print("Mean:"+str(round(nestle_monthly_returns.mean(),3)))  
print("Sample Standard Deviation:"+str(round(nestle_monthly_returns.std(axis=0),3)))

print(nestle_monthly_returns)