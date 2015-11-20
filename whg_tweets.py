import tweepy
from time import sleep, localtime, strftime
import sys

### User-defined modules
from lib.config_parser import Config
from lib.tweet_list import Tweets

### Configuration
CONFIG_DIR = '/etc/opt/whg_tweetsd/config.json'
config = Config(CONFIG_DIR).values

### Twitter authorization
auth = tweepy.OAuthHandler(config['auth']['consumer_token'], config['auth']['consumer_secret'])
auth.set_access_token(config['access_token']['key'], config['access_token']['secret'])

twitter = tweepy.API(auth)

tweets = Tweets(twitter,
    config['location'],
    config['last_checked_id'],
    config['keywords'],
    excluded = config['excluded_uids'])

if __name__ == "__main__":
    while True:
      for tweet in tweets.get_ids():
        try:
          result = twitter.retweet(tweet)
          sys.stdout.write("STATUS: Tweeted at " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n")
          sys.stdout.write("STATUS: Tweet Text: " + result.text.encode('utf8') + "\n")
          sys.stdout.write("STATUS: Tweet ID: " + str(result.id) + "\n")
          sys.stdout.write("STATUS: Last checked ID == " + str(tweets.lastCheckedId) + "\n")
        except tweepy.TweepError as e:
          sys.stderr.write("ERROR: " + str(e) + "\n")
          try:
            result = twitter.get_status(tweet)
            sys.stderr.write("ERROR: Error'd tweet ID = " + str(result.id) + "\n")
            sys.stderr.write("ERROR: Error'd tweet text = " + result.text.encode('utf8') + "\n")
          except AttributeError as e:
            sys.stderr.write("ERROR: " + str(e) + "\n")

      print "SLEEP: Sleeping for ", config['interval_secs'], " seconds at", strftime("%Y-%m-%d %H:%M:%S", localtime())
      sleep(config['interval_secs'])
      print "SLEEP: Finished sleeping. Restarting search at", strftime("%Y-%m-%d %H:%M:%S", localtime())
