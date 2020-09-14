import requests
from bs4 import BeautifulSoup

##1boon 공유많은 글
def oneboon_post():
    c_url = "https://1boon.kakao.com/p/share"
    title = "oneboon_post"
    data = ""

    def crawl(c_url):
        r = requests.get(c_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        list = soup.find('ol',{"class":"list_classify"}).findAll('a',{"class":"link_classify"})
        data = ""

        for lists in list:
            data = data + lists.get_text() + 'https://1boon.kakao.com' + lists['href'] ##링크 추가 02.06
            data = data +"yahait"

        return data
    data = crawl(c_url)
    print(title, data)
    return title, data







