# fbScrapper
<h2>How to run:</h2>

```shell
$ python3 script.py -h
usage: script.py [-h] [-url URL] [-b B] [-n N]

optional arguments:
  -h, --help  show this help message and exit
  -url URL    Url of facebook search ads page
  -b B        Name of the browser, firefox is default
  -n N        Folder name to save data and upload to google drive
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

![GIF](https://i.ibb.co/ws7mkFD/ezgif-com-video-to-gif.gif)

# Crontab Scheduler
<h2>How to run:</h2>

```shell
$ python3 scheduler.py -h
usage: scheduler.py [-h] [-url URL] [-b B] [-n N] [-m M] [-hour HOUR] [-d D] [-mon MON] [-dow DOW]

optional arguments:
  -h, --help  show this help message and exit
  -url URL    Url of the search page of facebook
  -b B        Name of the browser to be used, firefox is default
  -n N        Name of the folder to save data, and upload to google drive
  -m M        Minutes interval between automatic searches, 1 - 59
  -hour HOUR  Hours interval between automatic searches, 1 - 23
  -d D        Day of the month to program automatic searches, 1 a 31
  -mon MON    Month to program automatic searches, 1 a 12
  -dow DOW    Day of the week to program automatic searches, 0 a 7

```

> Example: Every 5 days, teste folder, using Google Chrome

```shell
(env) $ python3 scheduler.py -d "5" -n "teste" -b "Chrome" -url "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&impression_search_field=has_impressions_lifetime&view_all_page_id=13892765435&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped"
```

# Crontab Scheduler
<h2>How to stop the crontab:</h2>

### Delete all cron jobs

![GIF](https://i.ibb.co/y8qCx2F/pt1.gif)


### Kill all cron processes

> Use HTOP to find all cron jobs

> Write down all cron processes PIDs

> Use 'sudo kill' to kill all cron processes

### Reload cron service

![GIF](https://i.ibb.co/2N5jMBn/Cron-Reload.gif)