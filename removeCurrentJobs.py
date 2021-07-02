#!/usr/bin/env python

from crontab import CronTab
cron = CronTab(user='pi')


for job in cron:
    print(job)

cron.remove_all()

cron.write()