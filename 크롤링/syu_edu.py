import requests
from bs4 import BeautifulSoup
#삼육대학교 학사공지
def syu_edu():
    c_url = "https://new.syu.ac.kr/academic/academic-notice/"
    title = "syu_edu"
    data=""

    def crawl(c_url):
        r = requests.get(c_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        list = soup.find('div', {"class": "md_notice_bx"}).findAll('a', {"class": "itembx"})
        data = ""

        for ko in list:
            data = data + ko.get_text() + '\t' + ko['href'] + '\t' ##링크 추가 02.06
            data = data+"yahait"

        return data

    data = crawl(c_url)
    print(title, data)
    return title, data
