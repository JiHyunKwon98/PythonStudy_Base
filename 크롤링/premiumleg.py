#프리미엄리그 순위
from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('C:\chrome\chromedriver.exe', options=options)
driver.implicitly_wait(1)
driver.get('https://www.premierleague.com/tables')
html = driver.page_source
rows = BeautifulSoup(html,'html.parser')

club = rows.find_all("span", {"class": "long"})

for line in club:
    print(line.string+'\n')
file = open('text.txt','w',encoding='utf-8')
for i in club:
    file.write(i.string+'\n')
driver.quit()

