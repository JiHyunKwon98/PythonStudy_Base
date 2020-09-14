import requests
from bs4 import BeautifulSoup
##위비티 공모전,대외활동 목록
def wevity_international_activity():
    c_url = "https://www.wevity.com/?c=find&s=1&gp=1"
    title = "naver_stockmarket"
    data = ""

    def crawl(c_url):
        r = requests.get(c_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        list = soup.select(
            'ul.list > li > div.tit > a'
        )
        data = ""
        for ko in list:
            data = data + ko.get_text()  + '\t' + 'https://www.wevity.com/' + ko['href'] + '\t'##링크 추가 02.06
            data = data+"yahait"

        return data

    data = crawl(c_url)
    print(title, data)
    return title, data





