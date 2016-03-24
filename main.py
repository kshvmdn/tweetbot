import datetime
import argparse
import auth as keys
from twitterbot import TwitterBot
from apscheduler.schedulers.blocking import BlockingScheduler

parser = argparse.ArgumentParser(description='Respond to Twitter mentions.',
                                 epilog='example: main.py -l "happy birthday" \
                                         "hbd" -r "thanks HANDLE!"')
parser.add_argument('-l', '--listen', nargs='+', default=['happy birthday'],
                    help='phrase(s) to reply to (separate by space)')
parser.add_argument('-r', '--reply', default='HANDLE thanks!',
                    help='reply text (use HANDLE for user handle)')


# instantiate TwitterBot outside of main since it's required for reply
args = parser.parse_args()
bot = TwitterBot(keys, args.listen, args.reply.replace('HANDLE', '@{}'))


def reply(bot=bot):
    print(' Running...')
    bot.reply_to_mention()
    print(' Finished running at {}'.format(datetime.datetime.now()))


def main():
    print('Starting bot...')
    # start loop, run once every 2 minutes
    scheduler = BlockingScheduler()
    scheduler.add_job(reply, 'interval', minutes=2)
    scheduler.start()

if __name__ == '__main__':
    main()
