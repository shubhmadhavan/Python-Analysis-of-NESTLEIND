import requests
from bs4 import BeautifulSoup

nameOfStock='NESTLEIND.NS'     #changing this would allow us to scrape for other stocks
period1='1554076800'        #the date 01-04-2019 in seconds           
period2='1585699200'        #the date 31-03-2020 in seconds
#these are the dates in seconds from 'epoch' of human calender
#we can conveniently find out these dates using a simple calculator as on https://www.epochconverter.com/
# otherwise, formula for date to seconds is ((no of years from January 1, 1970 )*31556926)+(no of months*2629743)+ (no of days*86400 )

stock_url='https://query1.finance.yahoo.com/v7/finance/download/'+nameOfStock+'?period1='+period1+'&period2='+period2+'&interval=1d&events=history'
#genreral url using elementary concatenation to make our code more flexible

response=requests.get(stock_url, allow_redirects=True)
#now we have the html code of the NSE webpage

open('D:/'+nameOfStock+'.csv', 'wb').write(response.content)
