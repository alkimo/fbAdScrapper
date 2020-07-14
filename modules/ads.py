import os
import time
import io
from PIL import Image
from time import gmtime, strftime
import getpass
from selenium.webdriver.common.keys import Keys



def save_ad_pictures(driver, folder_path):
    driver.execute_script("document.body.style.transform = 'scale(0.9)'")
    scroll_to_page_floor(driver)
    images = driver.find_elements_by_class_name('_99s5')
    iterator = 1
    for image in images:
        image = image.screenshot_as_png
        imageStream = io.BytesIO(image)
        im = Image.open(imageStream)
        im.save(folder_path + '/ ' + str(iterator) + '.png')
        iterator += 1


def create_ads_folder(name , path):
    try:
        folder_path = path + 'searchResult/' + name
        os.mkdir(folder_path)
        return folder_path
    except:
        time_now = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
        folder_path = path + 'searchResult/' + name + '-' + time_now
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
