# Twitter AutoReply
Automatically respond to tweets that contain a specific string. Built with [Tweepy](http://www.tweepy.org) and [APScheduler](https://apscheduler.readthedocs.org/en/latest/).

### Usage

**Requirements**: Python 3

+ Fork/clone project, install requirements.

  ```
  $ git clone https://github.com/kshvmdn/twitter-autoreply.git && cd twitter-autoreply
  ```
  
+ Install requirements

  ```
  $ pip install -r requirements.txt
  ```

+ Setup a [Twitter app](https://apps.twitter.com). Place Consumer Key, Consumer Secret, Access Token, Access Token Secret in their respective spots in `auth.py`. **You will likely need to request an Access Token, Access Token Secret on the Twitter app.**

+ Run `main.py`. This will run once every minute. 
  ```
  optional arguments:
  -h, --help        show this help message and exit
  -l , --listen     mention text (default: 'happy birthday')
  -r , --response   response text (default: 'HANDLE thanks!') [use HANDLE for user handle]
  
  examples:
  $ python3 main.py -l 'GitHub is down!' -r 'Hey HANDLE, we're working on it! Sorry for the inconvenience'
  ```

### Contribute

This project is completely open source, feel free to open an [issue](https://github.com/kshvmdn/twitter-autoreply/issues) or make a [PR](https://github.com/kshvmdn/twitter-autoreply/pulls). All contributions are welcome! 
