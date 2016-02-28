# Twitter AutoReply
Automatically respond to tweets that contain a specific string. Built with [Tweepy](http://www.tweepy.org) and [APScheduler](https://apscheduler.readthedocs.org/en/latest/).

### Usage

**Requirements**: Python 3

+ Clone, setup project locally
  ```
  $ git clone https://github.com/kshvmdn/twitter-autoreply.git && cd twitter-autoreply # clone project
  ```

  ```
  $ pip install -r requirements.txt # install Python requirements
  ```
  
  ```
  $ mv auth.sample.py auth.py # rename auth.sample.py
  ```
  
+ Setup the [Twitter app](https://apps.twitter.com), add your tokens (all 4) to `auth.py`. You will need to request an __Access Token__ and __Access Token Secret__.

+ Run `main.py`. This will reply to new mentions once every minute. 

  ```
  optional arguments:
    -h, --help        show this help message and exit
    -l, --listen      phrase(s) to listen for and reply to (default=['happy birthday'])
    -r, --reply       reply text (default='HANDLE thanks!') [use HANDLE for user handle]
  
  examples:
    $ python3 main.py -l 'GitHub is down!' -r 'Hey HANDLE, we're working on it! Sorry for the inconvenience!'
    $ python3 main.py -l 'happy birthday' 'hbd' 'happy bday!'  # response will default to 'HANDLE thanks!'
  ```

### Contribute

This project is completely open source, feel free to open an [issue](https://github.com/kshvmdn/twitter-autoreply/issues) or make a [PR](https://github.com/kshvmdn/twitter-autoreply/pulls). All contributions are welcome! 
