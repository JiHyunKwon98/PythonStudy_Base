import requests
from bs4 import BeautifulSoup

c_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8"

def crawl(c_url):
    r = requests.get(c_url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    list = soup.find('dd', {"class": "weather_item _dotWrapper"}).findAll('span')

    lee = ""
    for ko in list:
        lee = lee + ko.get_text()
        lee = lee

    return lee

def crawl1(c_url):
    r = requests.get(c_url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    list = soup.find('ul', {"class": "info_list"}).findAll('p', {"class": "cast_txt"})

    lee = ""

    for ko in list:
        lee = lee +"오늘 날씨 : "+ ko.get_text()
        lee = lee

    return lee

def crawl2(c_url):
    r = requests.get(c_url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    list = soup.select('div.sub_info > div > dl > dd:nth-child(2)')

    lee = ""
    for ko in list:
        lee = lee+"미세먼지 : " + ko.get_text()
        lee = lee

    return lee

def crawl3(c_url):
    r = requests.get(c_url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    list = soup.select('div.sub_info > div > dl > dd:nth-child(4)')

    lee = ""
    for ko in list:
        lee = lee+"초미세먼지 : " + ko.get_text()
        lee = lee

    return lee

han = crawl(c_url)
han1 = crawl1(c_url)
han2 = crawl2(c_url)
han3 = crawl3(c_url)

print(han)
print(han1)
print(han2)
print(han3)

