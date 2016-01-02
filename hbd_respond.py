from twitterbot import TwitterBot

import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def say_thanks():
    bot = TwitterBot()
    bot.respond('happy birthday', '{0} thanks!')
    print(datetime.datetime.now())
    time.sleep(20)

scheduler.configure(say_thanks(), minute='0-1')
