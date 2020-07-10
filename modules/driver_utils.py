from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import os
import pdfkit 
import getpass


def select_driver(browser):
    if browser == "Chrome" or browser == "chrome":
        driver_path = '/home/' + getpass.getuser() +  '/Desktop/fbScrapper/driver/Chromedriver/chromedriver'
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        return webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
    elif browser == "Firefox" or browser == "firefox":
        driver_path = '/home/' + getpass.getuser() + '/Desktop/fbScrapper/driver/Gecko/geckodriver'
        return webdriver.Firefox(executable_path=driver_path)


def save_as_pdf(path_to_data):
    pdfkit.from_file(path_to_data + 'ads.html', path_to_data + 'ads.pdf') 
