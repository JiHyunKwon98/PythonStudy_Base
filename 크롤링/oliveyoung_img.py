import urllib.request
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('C:\chrome\chromedriver.exe', options=options)
driver.implicitly_wait(1)
url = 'http://www.oliveyoung.co.kr/store/main/getSaleList.do?dispCatNo=900000100090001&fltDispCatNo=&prdSort=01&pageIdx=1&rowsPerPage=24&searchTypeSort=btn_thumb'
folder_name = "images"   # 이 폴더 안에
file_name = "image"

driver.get(url)
count = 0
img = driver.find_elements_by_tag_name("img")
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




