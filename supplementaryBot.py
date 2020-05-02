from pytrends.request import TrendReq
import pandas as pd 
import wikipedia
import tweepy
import random


# Keys for authentication
CONSUMER_KEY = 'ItdSIzZCtPi2jxeuenxuHtEEp'
CONSUMER_SECRET = 'dLS8xt8DSsuVfxSfOdZvrM86IxvasolYZ9wU8ZDD0BcuXU1Nyl'
ACCESS_KEY = '1249506273831161856-MgdRnM0Q7PRQTtkZ6dwIurQJZTC1nl'
ACCESS_SECRET = 'lhP9AjMrPM7GdrzQg8Dlj9YfFTaE6cwyYWFgClhruzh2R'


# Retriving trends data from Google (global)
pytrend = TrendReq()
df = pytrend.trending_searches()                                            # Search for 
alpha = random.randint(0, 5)                                                # Choosing a random number of trend
print('Trend number: ', alpha)
trend = df.values[alpha]                                                    # Passes on numero uno
listToStr = ' '.join(map(str, trend))           
strToList = list(listToStr.split(' '))          
print(strToList)


# Searching Wikipedia for appropriate articles
searched_titles = []
for i in strToList:
    retrived_titles = wikipedia.search(i, results=3, suggestion=False)      # value of "results" dictates ammount of searched items
    searched_titles.append(retrived_titles)
print(searched_titles)

retrived_titles_modified = sum(searched_titles, [])                         # Joining list of lists
print(retrived_titles_modified)
randomized_title = random.choice(retrived_titles_modified)
print('Random title:', randomized_title)