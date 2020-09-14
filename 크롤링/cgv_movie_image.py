import urllib.request
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('C:\chrome\chromedriver.exe', options=options)
driver.implicitly_wait(1)
url = 'http://www.cgv.co.kr/movies/?ft=0'
folder_name = "movie"   # 이 폴더 안에
file_name = "movies"

driver.get(url)
count = 0
img = driver.find_elements_by_css_selector('#contents > div.wrap-movie-chart > div.sect-movie-chart > ol > li > div.box-image > a > span > img')
##기존의 img = driver.find_elements_by_tag_name("img") 를 selector로 바꾸어 필요한 사진만 크롤링 02.06
for item in img:
    if (count > 0 and count < 105):
        full_name = "C:\python\crawling\\" + folder_name + "\\" + file_name + str(count) + ".jpg"
        try:
            urllib.request.urlretrieve(item.get_attribute('src'), full_name)
            print(item.get_attribute('src')[:30] + " : ")
        except:
            urllib.request.urlretrieve(item.get_attribute('data-src'), full_name)
            print(item.get_attribute('data-src')[:30] + " : ")
        print("{0}. Saving : {1}".format(count, full_name))
    count = count + 1