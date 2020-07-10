from bs4 import BeautifulSoup as bs
import os
import getpass


def save_html(driver, ads_folder_path):
    html = driver.execute_script("return document.body.innerHTML;")
    soup = bs(html, 'html.parser')

    driver.close()
    ads = soup.find_all("div", class_="_8n-_")

    with open('/home/' + getpass.getuser() + '/Desktop/fbScrapper/template.html', 'r') as f:
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