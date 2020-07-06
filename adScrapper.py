import modules.parser
import modules.html
import modules.ads
import modules.driver_utils
import modules.api
import time
from random import randint
import os


def treat_cli_name(name):
    a = os.getcwd() + '/searchResult/' + name + '/'
    random_value=name

    if(os.path.isdir(a) == True):
        b = os.getcwd() + '/searchResult/' + name + '/'
        while(a == b):
            random_value=name + '-' + str(randint(100, 999))
            a = os.getcwd() + '/searchResult/' + name + '-' + str(randint(100, 999)) + '/'
    return random_value
    


def main():
    cli_input = modules.parser.initParse()
    cli_input.n = treat_cli_name(cli_input.n)
    driver = modules.driver_utils.select_driver(cli_input.b)
    ads_folder_path = modules.ads.create_ads_folder(cli_input.n)
    driver.get(cli_input.url)
    modules.ads.save_ad_pictures(driver, ads_folder_path)
    modules.html.save_html(driver, ads_folder_path)
    modules.driver_utils.save_as_pdf(ads_folder_path + '/')
    modules.api.upload(cli_input.n, os.getcwd() + '/searchResult/' + cli_input.n + '/')

if __name__ == "__main__":
    main()