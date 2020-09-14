import requests
from bs4 import BeautifulSoup
#네이버 금융 인기검색  종목 순위

def naver_stockmarket():
    c_url = "https://finance.naver.com/sise/lastsearch2.nhn"
    title = "naver_stockmarket"
    data = ""

    def crawl(c_url):
        r = requests.get(c_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        list = soup.find('table',{"class":"type_5"}).findAll('a',{"class":"tltle"})
        data = ""

        title = soup.findAll('td',{"class":"no"})

        for ko in list :
            data = data+ ko.get_text()
            data = data+"yahait"

        return data

    data = crawl(c_url)
    print(title, data)
    return title, data

