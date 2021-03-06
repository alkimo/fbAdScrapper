import argparse
import time


def initParse():
    # Initiate the parser
    parser = argparse.ArgumentParser()

    # Link da pesquisa do facebook ads
    parser.add_argument("-url", help="Url do ad do facebook")

    # Nome do browser a ser usado
    parser.add_argument("-b", help="Browser a ser utilizado: Chrome ou Firefox")

    # Nome da pasta para salvar os dados
    parser.add_argument("-n", help="Nome da pasta a ser salvo os dados")

    # Read arguments from the command line
    args = parser.parse_args()

    if(args.url == None):
        args.url = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&impression_search_field=has_impressions_lifetime&view_all_page_id=59685491632&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped"

    if(args.b == None):
        args.b = "Firefox"

    if(args.n == None):
        args.n = time.strftime("%Y%m%d-%H%M%S")

    return args