# TwitterBirthdayResponder
Automatically respond to all 'Happy Birthday' tweets. Built with [Tweepy](http://www.tweepy.org), [APScheduler](https://apscheduler.readthedocs.org/en/latest/).

## Usage

**Requirements**: Python 3, a Twitter account (I guess, lol)

Fork/clone project, install requirements (Python 3).
```
$ git clone https://github.com/kshvmdn/TwitterBirthdayResponder.git && pip3 install -r ./requirements.txt
```

Setup [Twitter app](https://apps.twitter.com), replace Consumer Key (API Key), Consumer Secret (API Secret), Access Token, Access Token Secret with `consumer_key`, `consumer_secret`, `access_token`, `access_token_secret` in `keys.txt`. **You will likely need to request Access Token + Access Token Secret on the Twitter app.**

Edit `bot.respond('happy birthday', '@{0} thanks!')` [line 12, `respond_to_mention.py`], if you want a personalized response. `{0}` represents the username being responded to.

Run `respond_to_mention.py`. This will run once every other minute. Edit `scheduler.add_job(respond, 'interval', minutes=2)` [line 18] to change interval. Get more info in the APScheduler [documentation](https://apscheduler.readthedocs.org/en/latest/).
