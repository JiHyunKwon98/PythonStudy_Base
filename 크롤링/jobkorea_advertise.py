import requests
from bs4 import BeautifulSoup
#잡코리아 best채용공고
def jobkorea_advertise():
    c_url = "http://www.jobkorea.co.kr/top100/"
    title = "jobkorea_advertise"
    data=""

    def crawl(c_url):
        r = requests.get(c_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        list = soup.select(
            'div.info > div.tit > a '
        )
        data = ""
        for ko in list:
            data = data + ko.get_text()+ '\t' + 'http://m.jobkorea.co.kr' + ko['href'] + '\t' ##링크 추가 02.06
            data = data+"yahait"

        return data

    data = crawl(c_url)
    print(title, data)
    return title, data


