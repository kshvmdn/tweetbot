# TwitterBirthdayResponder
Automatically respond to all 'Happy Birthday' tweets. Built with [Tweepy](http://www.tweepy.org), [APScheduler](https://apscheduler.readthedocs.org/en/latest/).

## Usage

**Requirements**: Python 3, a Twitter account (I guess, lol)

Fork/clone project, install requirements (Python 3).
```
$ git clone https://github.com/kshvmdn/TwitterBirthdayResponder.git && pip3 install -r ./requirements.txt
```

Setup [Twitter app](https://apps.twitter.com), replace Consumer Key (API Key), Consumer Secret (API Secret), Access Token, Access Token Secret with `consumer_key`, `consumer_secret`, `access_token`, `access_token_secret` in `keys.txt`. **You will likely need to request Access Token + Access Token Secret on the Twitter app.**

Edit `bot.respond('happy birthday', '{0} thanks!')` [line 12, `hbd_respond.py`], if you want a personalized response. `{0}` represents the username being responded to.

Run `hbd_response.py`. This will run once a minute. Edit `scheduler.configure(say_thanks(), minute='0-1')` [line 18] to change time limit. Get more info in the APScheduler [documentation](https://apscheduler.readthedocs.org/en/latest/).
