import urllib.request
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('C:\chrome\chromedriver.exe', options=options)
driver.implicitly_wait(1)
url = 'https://1boon.kakao.com/p/share'
folder_name = "1boon"  # 이 폴더 안에
file_name = "1boons"
driver.get(url)
count = 0
img = driver.find_elements_by_css_selector('#mArticle > div > ol > li> a > span > span > img.img_thumb')
for item in img:
    if (count > 0 and count < 105):
        full_name = "C:\python\crawling\\" + folder_name + "\\" + file_name + str(count) + ".jpg"
        try:
            urllib.request.urlretrieve(item.get_attribute('src'), full_name)  # src를 받는다.
            print(item.get_attribute('src')[:30] + " : ")
        except:
            urllib.request.urlretrieve(item.get_attribute('data-src'), full_name)
            print(item.get_attribute('data-src')[:30] + " : ")
        print("{0}. Saving : {1}".format(count, full_name))
    count = count + 1

