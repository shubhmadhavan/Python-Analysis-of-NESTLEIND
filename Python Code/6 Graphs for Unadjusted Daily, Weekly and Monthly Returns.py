import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web


df = web.get_data_yahoo("NESTLEIND.NS",
                            start = "2019-04-01",
                            end = "2020-03-31")        
                            #adds reproducability of code and flexibility of time period    
df['Daily_Return']=df['Close'].pct_change(1)
                            #Daily Returns have been stored in a separate column
df['Daily_Return']=df['Daily_Return']*100                          
df['Daily_Return'].plot(kind='line',title='Line Graph for Daily Returns')
plt.show()

Weekly=pd.DataFrame(columns=['Weekly_Return'])
Weekly['Weekly_Return'] =df ['Close'].resample('W-FRI').ffill().pct_change()   
Weekly['Weekly_Return'] =Weekly['Weekly_Return'] *100
                            #resampling by weekly data with Friday as the anchor
                            #even if the Friday is a holiday, the previous day is taken and filled in that day                                

Weekly['Weekly_Return'].plot(kind='line',title='Line Graph for Weekly Returns')
plt.show()


Monthly=pd.DataFrame(columns=['Monthly_Return'])
Monthly['Monthly_Return'] =df ['Close'].resample('M').ffill().pct_change()   
                            #resampling by weekly data with Friday as the anchor
                            #even if the Friday is a holiday, the previous day is taken and filled in that day                                
Monthly['Monthly_Return']=Monthly['Monthly_Return']*100

Monthly['Monthly_Return'].plot(kind='line',title='Line Graph for Monthly Returns')
plt.show()