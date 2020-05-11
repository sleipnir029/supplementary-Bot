from pytrends.request import TrendReq
import pandas as pd 
import wikipedia
import tweepy
import random


# Keys for authentication
CONSUMER_KEY = 'consumerKey'
CONSUMER_SECRET = 'consumerSecret'
ACCESS_KEY = 'accessKey'
ACCESS_SECRET = 'accessSecret'


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


# Handling error on unsuccessful search results
wikipedia.set_lang("en")
try:
    complete_content = wikipedia.page(randomized_title, pageid=None,
                    auto_suggest=True, redirect=True, preload=False)
except wikipedia.DisambiguationError as e:                                   # if it raises, returns a list of titles of Wikipedia pages that the query may refer to.
    temp = random.choice(e.options)
    complete_content = wikipedia.page(temp)
    print('Random choice after Disambiguation Error: ', temp)
    print(temp, ' <--page contains this--> ', complete_content.content[:50])



# Getting content from articles and manipulating for status
page_url = complete_content.url
character_limit = 190 - len(page_url)
page_content = complete_content.content[:character_limit]
print(page_url, '\nurllen:', len(page_url), '\ncharlim:', character_limit,
    '\ncontent:', page_content, '....')                                         # sort of a debugger 🥱😎

tweet = page_content + '...' + '\n' + page_url
print(tweet)


# Setting up twitter authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.update_status(tweet)
print('====Done====')
