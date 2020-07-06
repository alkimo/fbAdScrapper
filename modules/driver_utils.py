from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import os
import pdfkit 



def select_driver(browser):
    if browser == "Chrome" or browser == "chrome":
        driver_path = os.getcwd() + '/driver/Chromedriver/chromedriver'
        return webdriver.Chrome(executable_path=driver_path)
    elif browser == "Firefox" or browser == "firefox":
        driver_path = os.getcwd() + '/driver/Gecko/geckodriver'
        return webdriver.Firefox(executable_path=driver_path)


def save_as_pdf(path_to_data):
    pdfkit.from_file(path_to_data + 'ads.html', path_to_data + 'ads.pdf') 
