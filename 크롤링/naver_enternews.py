import requests
from bs4 import BeautifulSoup
# 네어버 연예 추천뉴스 목록
def naver_enternews():
    c_url = "https://entertain.naver.com/ranking"
    title = "naver_enternews"
    data = ""

    def crawl(c_url):
        r = requests.get(c_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        list = soup.find('ul',{"class":"aside_airs_news_lst"}).findAll('a',{"class":"title"})
        data = ""

        for ko in list:
            data = data + ko.get_text() + '\t' + ko['href'] + '\t' ##링크 추가 02.06
            data = data+"yahait"

        return data

    data = crawl(c_url)
    print(title, data)
    return title, data







