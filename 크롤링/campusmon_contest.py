import requests
from bs4 import BeautifulSoup
#캠퍼스몬 공모전 best

def campusmon_contest():
    c_url = "http://campusmon.jobkorea.co.kr/Contest/Ranking"
    title = "campusmon_contest"
    data = ""

    def crawl(c_url):
        r = requests.get(c_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        list = soup.select(
            'tr > td.tl > p.ti > a'
        )
        data = ""

        for ko in list:
            data = data + ko.get_text() + '\t' + 'http://campusmon.jobkorea.co.kr' + ko['href'] + '\t' ##링크 추가 02.06
            data = data +"yahait"
        return data
    data = crawl(c_url)
    print(title, data)
    return title, data







