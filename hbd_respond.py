from twitterbot import TwitterBot

import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def say_thanks():
    bot = TwitterBot()
    bot.respond('test', '{0} hi!')
    print(datetime.datetime.now())
    time.sleep(20)

scheduler.configure(say_thanks(), minute='0-1')
