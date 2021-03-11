from newsapi import NewsApiClient
from decouple import config

api = NewsApiClient(api_key=config('APIKEY'))
top_headlines = api.get_top_headlines(
    country='in', category='sports', language='en')['articles']


def get_sports_news():
    for i in range(3):
        print(top_headlines[i]['title'])


get_sports_news()
