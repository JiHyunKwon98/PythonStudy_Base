import requests
from bs4 import BeautifulSoup
#네이버 경제  뉴스
def naver_ecomomynews():
    c_url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101"
    title = "naver_ecomomynews"
    data=""

    def crawl(c_url):
        r = requests.get(c_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        list = soup.find('ul',{"class":"section_list_ranking"}).findAll('a')
        data = ""
        for ko in list:
            data = data + ko.get_text()+ '\t' +'https://news.naver.com' + ko['href'] + '\t' ##링크 추가 02.06
            data = data+"yahait"

        return data

    data = crawl(c_url)
    print(title, data)
    return title, data




