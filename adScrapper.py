from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup as bs
from parser import initParse
import os
import time
from PIL import Image
import io
import time

###FIREFOX driver
# driverPath = os.getcwd() + '/driver/Gecko/geckodriver'
# driverType = "firefox"
# driver = webdriver.Firefox(executable_path=driverPath)

###CHROME driver

driverPath = os.getcwd() + '/driver/Chromedriver/chromedriver'
driverType = "chrome"
driver = webdriver.Chrome(executable_path=driverPath)

## Create Dir
myUrl = initParse()
timestr = time.strftime("%Y%m%d-%H%M%S")
filePath = os.getcwd() + '/searchResult/ ' + driverType + ' - ' + timestr
os.mkdir(filePath)
driver.get(myUrl.url)

## Saving Pictures code

time.sleep(1)

images = driver.find_elements_by_class_name('_99s5')
iterator = 1

for image in images:
    image = image.screenshot_as_png
    imageStream = io.BytesIO(image)
    im = Image.open(imageStream)
    im.save(filePath + '/ ' + str(iterator) + '.png')
    iterator += 1

last_height = driver.execute_script("return document.body.scrollHeight")

while(True):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height


## HTML saving
html = driver.execute_script("return document.body.innerHTML;")
soup = bs(html, 'html.parser')

driver.close()
ads = soup.find_all("div", class_="_8n-_")

with open('template.html', 'r') as f: 
        template = f.read()
        template_soup = bs(template, 'html.parser')

for ad in ads:
    main_div = template_soup.find("div", class_="_99s8")
    main_div.insert(1, ad)

floating_bar = template_soup.find(id="secondaryFiltersV2")
floating_bar.decompose()

buttons_div = template_soup.find("div", class_="_8ml1")
buttons_div.decompose()

search_bar = template_soup.find("div", class_="_8kew")
search_bar.decompose()

selects = template_soup.find_all("div", class_="_7kfi")

for match in selects:
    match.decompose()

Html_file = open(filePath + "/search.html","w")
Html_file.write(str(template_soup))
Html_file.close()