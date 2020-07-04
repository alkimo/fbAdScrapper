from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup as bs
import modules.parser
import os
import time
from PIL import Image
import io
import time


def select_driver(browser):
    if browser == "Chrome" or browser == "chrome":
        driver_path = os.getcwd() + '/driver/Chromedriver/chromedriver'
        return webdriver.Chrome(executable_path=driver_path)
    elif browser == "Firefox" or browser == "firefox":
        driver_path = os.getcwd() + '/driver/Gecko/geckodriver'
        return webdriver.Firefox(executable_path=driver_path)


def save_ad_pictures(driver, folder_path):
    scroll_to_page_floor(driver)
    images = driver.find_elements_by_class_name('_99s5')
    iterator = 1
    for image in images:
        image = image.screenshot_as_png
        imageStream = io.BytesIO(image)
        im = Image.open(imageStream)
        im.save(folder_path + '/ ' + str(iterator) + '.png')
        iterator += 1


def create_ads_folder(browser, name):
    folder_path = os.getcwd() + '/searchResult/ ' + browser + ' - ' + name
    os.mkdir(folder_path)
    return folder_path


def scroll_to_page_floor(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while(True):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def save_html(driver, ads_folder_path):
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

    Html_file = open(ads_folder_path + "/ads.html", "w")
    Html_file.write(str(template_soup))
    Html_file.close()


def main():
    cli_input = modules.parser.initParse()
    driver = select_driver(cli_input.b)

    ads_folder_name = cli_input.n if cli_input.n else time.strftime("%Y%m%d-%H%M%S")

    ads_folder_path = create_ads_folder(cli_input.b, ads_folder_name)
    driver.get(cli_input.url)
    save_ad_pictures(driver, ads_folder_path)
    save_html(driver, ads_folder_path)


if __name__ == "__main__":
    main()
