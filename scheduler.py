#!/usr/bin/python3

# import os
# from crontab import CronTab

# cron = CronTab(user='null')
# job = cron.new(command='/usr/bin/python3 /home/null/Desktop/fbScrapper/b.py')
# job.minute.every(2)

# cron.write()

import schedulerParser
from crontab import CronTab
import getpass

def main():
    scheduler_input = schedulerParser.initParse()
    

    arguments = []

    total_args = ''
    for arg in arguments:
        total_args += arg

    print(total_args)
    
    cron = CronTab(user='null')
    cron_search = 'source /home/' + getpass.getuser() + '/Desktop/fbScrapper/env/bin/activate; /home/null/Desktop/fbScrapper/env/bin/python3 /home/' + getpass.getuser() + '/Desktop/fbScrapper/script.py -n \"' + \
        scheduler_input.n + '\" -u \"' + scheduler_input.url + '\" -b \"' + scheduler_input.b + '\" > /home/' + getpass.getuser() +'/Desktop/erros.log 2>&1'
    
    job = cron.new(command=cron_search)

    try:
        if(scheduler_input.m and int(scheduler_input.m) > 0 and int(scheduler_input.m) < 60):
            job.minute.every(int(scheduler_input.m))
    except:
        pass

    try:
        if(scheduler_input.hour and int(scheduler_input.hour) > 0 and int(scheduler_input.hour) < 60):
            job.hour.every(int(scheduler_input.hour))
    except:
        pass

    try:
        if(scheduler_input.d and int(scheduler_input.d) > 0 and int(scheduler_input.m) < 32):
            job.day.every(int(scheduler_input.d))
    except:
        pass

    try:
        if(scheduler_input.mon and int(scheduler_input.mon) > 0 and int(scheduler_input.mon) < 13):
            job.month.every(int(scheduler_input.d))
    except:
        pass

    cron.write() 

if __name__ == "__main__":
    main()
