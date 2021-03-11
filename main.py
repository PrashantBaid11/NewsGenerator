from newsapi import NewsApiClient
from decouple import config
import random
from bs4 import BeautifulSoup
import requests

api = NewsApiClient(api_key=config('APIKEY'))


def get_news(category):
    return api.get_top_headlines(country='in', category=category,
                                 language='en')['articles']


def display_news(news, times=3):
    for i in range(times):
        print('- ' + news[random.randint(0, 15)]['title'])


def get_natinal_news():
    reponse = requests.get(
        'https://www.indiatoday.in/news.html')
    content = BeautifulSoup(reponse.text, 'html.parser')
    news = content.select('.news-columns')
    news = news[0].select('#card_1206578_itg-news-section-1')
    news = news[0].find_all('p')
    for headline in news:
        print('- ' + headline.get('title'))


def get_sports_news():
    sports_news = get_news('sports')
    display_news(sports_news)


print("#### NATIONAL NEWS ######")
get_natinal_news()
print("#### SPORTS NEWS ######")
get_sports_news()
