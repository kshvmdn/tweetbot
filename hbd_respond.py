import datetime

from twitterbot import TwitterBot
from apscheduler.schedulers.blocking import BlockingScheduler

user = TwitterBot()


def say_thanks():
    print('Running say_thanks.')
    user.respond('happy birthday!', '@{0} thanks!')
    print('Finished running at {0}'.format(datetime.datetime.now()))

# run once every 2 minutes
scheduler = BlockingScheduler()
scheduler.add_job(say_thanks, 'interval', minutes=2)
scheduler.start()
