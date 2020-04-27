import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web

df = pd.read_excel('T_bill_2018_2019_Daily.xlsx',index_col=[0]) 

df_Weekly  = df['T-Bill Return% (Daily)'].resample('W-FRI').ffill().apply(lambda x: x*365/52)
df_Monthly = df['T-Bill Return% (Daily)'].resample('M').ffill().apply(lambda x: x*365/12)


print(df_Weekly)