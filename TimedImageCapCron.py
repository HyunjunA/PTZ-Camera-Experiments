#!/usr/bin/env python

from crontab import CronTab
import pathlib

cron = CronTab(user='pi')


# for job in cron:
#     print(job)

# cron.remove_all()

# cron.write()

# for job in cron:
#     print(job)

'/bin/python /home/pi/Documents/PTZ-Camera-Controller/PTZ_IMX477_Controller/pyCode/TimedImageCapVer2.py'

filename="TimedImageCapVer2.py"
path=str(pathlib.Path.cwd())
# print(path+"/"+filename)
filePath=path+"/"+filename
pythonpath="/bin/python"
command=pythonpath+" "+filePath

# print(command)


with CronTab(user='pi') as cron:
    
    # job = cron.new(command='/bin/python /home/pi/Documents/PTZ-Camera-Controller/PTZ_IMX477_Controller/pyCode/TimedImageCapVer2.py')
    # job = cron.new(command='/bin/python /home/pi/Documents/PTZ-Camera-Controller/PTZ_IMX477_Controller/pyCode/TimedImageCapVer2.py')
    job = cron.new(command=command)
    
    job.minute.every(1)
print('cron.write() was just executed')


for job in cron:
    print(job)

print("Last line")

# cron.remove_all()

# for job in cron:
#     print(job)