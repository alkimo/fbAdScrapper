# fbScrapper
<h2>How to run:</h2>

```shell
$ python3 script.py -h
usage: script.py [-h] [-url URL] [-b B] [-n N]

optional arguments:
  -h, --help  show this help message and exit
  -url URL    Url do ad do facebook
  -b B        Browser a ser usado
  -n N        Nome da pasta a salvar os dados
```

## Installation

- Clone repo 
- Initialize libraries
- Generate token
- Allow permits

### Clone repo

> Clone this repo to your local machine 

```shell
$ git clone git@github.com:alkimo/fbAdScrapper.git
```

### Initialize libraries

> Initialize all libraries with pip install on requirements.txt

```shell
$ cd fbAdScrapper
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip3 install -r requirements.txt
```

### Run test

> Run test to generate token
```shell
(env) $ python3 script.py -n "Teste"
```

### Allow all permits

![Recordit GIF](https://im4.ezgif.com/tmp/ezgif-4-eb032f92cf6f.gif)

# Crontab Scheduler
<h2>How to run:</h2>

```shell
$ python3 scheduler.py -h
usage: scheduler.py [-h] [-url URL] [-b B] [-n N] [-m M] [-hour HOUR] [-d D] [-mon MON] [-dow DOW]

optional arguments:
  -h, --help  show this help message and exit
  -url URL    Url do ad do facebook
  -b B        Primeiro valor de pesquisa
  -n N        Nome da pasta a salvar os dados
  -m M        Minutos de intervalo para repetição do script pelo crontab, 0 a 59
```

> Example: Every 5 days, teste folder, using Google Chrome

```shell
(env) $ python3 scheduler.py -d "5" -n "teste" -b "Chrome" -url "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&impression_search_field=has_impressions_lifetime&view_all_page_id=13892765435&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped"
```