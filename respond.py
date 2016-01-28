import datetime
import argparse

from kshvmdn import twitter
from twitterbot import TwitterBot
from apscheduler.schedulers.blocking import BlockingScheduler

parser = argparse.ArgumentParser(description='Respond to Twitter mentions.')
parser.add_argument('-l', '--listen', metavar='', default='happy birthday',
                    help='mention text to listen for')
parser.add_argument('-r', '--response', metavar='', default='HANDLE thanks!',
                    help='response text (use HANDLE for user handle)')
args = parser.parse_args()

bot = TwitterBot(twitter, args.listen, args.response.replace('HANDLE', '@{}'))


def main():
    print('Running...')
    bot.respond_to_mention()
    print('Finished running at {}'.format(datetime.datetime.now()))

# run once every 2 minutes
scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', minutes=2)
scheduler.start()
