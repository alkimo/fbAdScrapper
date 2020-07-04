import argparse

def initParse():
    # Initiate the parser
    parser = argparse.ArgumentParser()

    # Add long and short argument
    parser.add_argument("-url", help="Primeiro valor de pesquisa")

    # Read arguments from the command line
    args = parser.parse_args()

    if(args.url == None):
        args.url = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&impression_search_field=has_impressions_lifetime&view_all_page_id=59685491632&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped"

    return args