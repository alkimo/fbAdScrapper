import modules.parser
import modules.html
import modules.ads
import modules.driver_selection
import time
import api
import os
from random import randint


def main():
    cli_input = modules.parser.initParse()

    a = os.getcwd() + '/searchResult/' + cli_input.n + '/'


    if(os.path.isdir(a) == True):
        b = os.getcwd() + '/searchResult/' + cli_input.n + '/'
        while(a == b):
            random_value=cli_input.n + '-' + str(randint(100, 999))
            a = os.getcwd() + '/searchResult/' + cli_input.n + '-' + str(randint(100, 999)) + '/'
        cli_input.n=random_value

    driver=modules.driver_selection.select_driver(cli_input.b)
    ads_folder_path=modules.ads.create_ads_folder(cli_input.n)
    driver.get(cli_input.url)
    modules.ads.save_ad_pictures(driver, ads_folder_path)
    modules.html.save_html(driver, ads_folder_path)
    api.upload(cli_input.n, os.getcwd() + '/searchResult/' + cli_input.n + '/')

if __name__ == "__main__":
    main()
