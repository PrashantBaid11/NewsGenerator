from bs4 import BeautifulSoup
import requests


def get_news(id, index=0):
    reponse = requests.get(
        'https://www.indiatoday.in/news.html')
    content = BeautifulSoup(reponse.text, 'html.parser')
    news = content.select('.news-columns')
    news = news[index].select(id)
    news = news[0].find_all('p')
    for headline in news:
        print('- ' + headline.get('title'))


def get_international_news():
    reponse = requests.get("https://www.indiatoday.in/world")
    content = BeautifulSoup(reponse.text, 'html.parser')
    news = content.select('.catagory-listing')
    for i in range(len(news)):
        print('- ' + news[i].select('.detail')
              [0].find_all('h2')[0].get('title'))


def get_national_news():
    get_news("#card_1206578_itg-news-section-1")


def get_sports_news():
    get_news("#card_1206550_itg-news-section-4", 3)


print("##### INTERNATIONAL NEWS ######")
get_international_news()

print("##### NATIONAL NEWS ######")
get_national_news()

print("#####SPORTS NEWS ######")
get_sports_news()
