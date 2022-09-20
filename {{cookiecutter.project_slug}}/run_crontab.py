"""
This file is used to run `crontab_call_schedule.py` (the scheduler you have set up)
So you can remove it and `crontab_call_schedule.py` if you don't need scheduler like AWS EventBridge
"""

import argparse
import os
import sys

from app.logger.logger import configure_logging

logger = configure_logging(__name__)

"""You need to add crontab to poetry"""
from crontab import CronTab

my_cron = CronTab(user=True)


def remove_all_crontab():
    my_cron.remove_all()
    my_cron.write()


def start_schedule(minutes=1):
    remove_all_crontab()
    command = 'cd ' + os.getcwd() + ' && ' + \
              os.path.dirname(sys.executable) + '/python ' + os.getcwd() \
              + '/crontab_call_schedule.py'
    print(command)
    job = my_cron.new(command=command)
    job.minute.every(minutes)
    my_cron.write()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Choose a type crontab.")
    parser.add_argument("-n", "--number",
                        help="0 to remove all task, any number to start schedule with minutes corresponding",
                        default=1)
    choose = 1
    try:
        args = parser.parse_args()
        choose = int(args.number)
    except:
        print("args fail")
    if choose == 0:
        remove_all_crontab()
        logger.info("Remove All Crontab")
    else:
        start_schedule(minutes=choose)
        logger.info("Start schedule")
