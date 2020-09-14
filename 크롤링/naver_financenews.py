import requests
from bs4 import BeautifulSoup
#네이버 금융 주요뉴스
def naver_financenews():
    c_url = "https://finance.naver.com/"
    title = "naver_financenews"
    data = ""

    def crawl(c_url):
        r = requests.get(c_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        list = soup.find('div',{"class":"section_strategy"}).findAll('a')
        data = ""
        for ko in list:
            data = data + ko.get_text() + '\t' + 'https://finance.naver.com' + ko['href'] + '\t'##링크 추가 02.06
            data = data+"yahait"

        return data

    data = crawl(c_url)
    print(title, data)
    return title, data


