import datetime
import argparse

from auth import twitter_auth as auth
from twitterbot import TwitterBot
from apscheduler.schedulers.blocking import BlockingScheduler

parser = argparse.ArgumentParser(description='Respond to Twitter mentions.')
parser.add_argument('-l', '--listen', metavar='', nargs='+', default='happy birthday',
                    help='phrase[s] to reply to (separate by space)')
parser.add_argument('-r', '--response', metavar='', default='HANDLE thanks!',
                    help='response text (use HANDLE for user handle)')
args = parser.parse_args()

bot = TwitterBot(auth, args.listen, args.response.replace('HANDLE', '@{}'))


def respond():
    print(' Running...')
    bot.respond_to_mention()
    print(' Finished running at {}'.format(datetime.datetime.now()))


def main():
    # print('Starting bot...')
    #
    # # run once every minute
    # scheduler = BlockingScheduler()
    # scheduler.add_job(respond, 'interval', minutes=1)
    # scheduler.start()
    respond()

if __name__ == '__main__':
    main()
