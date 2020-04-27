import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web

df = web.get_data_yahoo("NESTLEIND.NS",
                            start = "2019-04-01",
                            end = "2020-03-31")       
df.to_csv (r'D:\000Finance\FOFA ASSIGNMENT 2\85_Shubh_2018A2PS0832H_DELTACORP\1 NESTLEIND.csv', header=True)

