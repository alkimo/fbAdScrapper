import argparse
import time


def initParse():
    # Initiate the parser
    parser = argparse.ArgumentParser()

    # Link da pesquisa do facebook ads
    parser.add_argument("-url", help="Url do ad do facebook")

    # Nome do browser a ser usado
    parser.add_argument("-b", help="Primeiro valor de pesquisa")

    # Nome da pasta para salvar os dados
    parser.add_argument("-n", help="Nome da pasta a salvar os dados")

    # Intervalo de minutos a se repetir, 0 a 59,
    parser.add_argument("-m", help="Minutos de intervalo para repetição do script pelo crontab, 0 a 59")

    # Intervalo de horas a se repetir, 0 a 23
    parser.add_argument("-hour", help="Horas de intervalo para repetição do script pelo crontab, 0 a 23")

    # Dias do mes a se repetir, 1 to 31
    parser.add_argument("-d", help="Dias do mes a se repetir, 1 a 31")

    # Mes a se repetir
    parser.add_argument("-mon", help="Nome da pasta a salvar os dados, 1 a 12")

    # Dia da semana a se repetir
    parser.add_argument("-dow", help="Nome da pasta a salvar os dados, 0 a 7")

    # Read arguments from the command line
    args = parser.parse_args()

    if(args.url == None):
        args.url = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=BR&impression_search_field=has_impressions_lifetime&view_all_page_id=59685491632&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped"

    if(args.b == None):
        args.b = "Chrome"

    if(args.n == None):
        args.n = time.strftime("%Y%m%d-%H%M%S")

    return args