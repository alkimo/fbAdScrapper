import os
import time
import io
from PIL import Image
from random import randint

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


def create_ads_folder(name):
    folder_path = os.getcwd() + '/searchResult/' + name +'/'
    path = folder_path

    if(os.path.isdir(folder_path) == True):
        while(folder_path == path):
            folder_path = os.getcwd() + '/searchResult/' + name + '-' + str(randint(100, 999)) + '/'

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
