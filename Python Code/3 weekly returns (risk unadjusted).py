import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web

nestle = web.get_data_yahoo("NESTLEIND.NS",
                            start = "2019-04-01",
                            end = "2020-03-31")

nestle_weekly_returns = nestle['Close'].resample('W-FRI').ffill().pct_change()    
                #resampling by weekly data with Friday as the anchor
                #even if the Friday is a holiday, the previous day is taken and filled in that day
nestle_weekly_returns=nestle_weekly_returns*100

print("Weekly Returns")
print("Maximum:"+ str(round(nestle_weekly_returns.max(axis=0),3)))    
print("Minimum:"+str(round(nestle_weekly_returns.min(axis=0),3)))  
print("Mean:"+str(round(nestle_weekly_returns.mean(),3)))  
print("Sample Standard Deviation:"+str(round(nestle_weekly_returns.std(axis=0),3))) 


