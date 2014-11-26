from sortedcontainers import SortedSet
import tweepy
import sys
from time import localtime, strftime

class Tweets():

  api = None
  lastCheckedId = None
  keywords = None
  lang = None
  journal = None
  location = None
  excluded = None

  def __init__(self, api, location, initialId, searchTerms, lang = 'en', journal = None, excluded = []):
    self.api = api
    self.location = location
    self.lastCheckedId = initialId
    self.searchTerms = searchTerms
    self.lang = lang
    self.journal = None
    self.excluded = excluded;
 
  ### Get all tweets from all search words in a list
  ### Filter out duplicate ids from the list
  ### Return the set of ids 
  def get_ids(self):

    tweetIds = SortedSet()

    for term in self.searchTerms:

      try:

        geo = self.location + ',' + term['distance']

        results = self.api.search(term['keyword'],
                                  self.lang,
                                  since_id = self.lastCheckedId,
                                  geocode = self.location + ',' + term['distance'])

        tweetIds.update([result.id for result in results if (result.author.id not in self.excluded)])

        if len(tweetIds) != 0:
          self.lastCheckedId = max(tweetIds)
        else:
          if self.journal is None:
            sys.stdout.write("STATUS: No tweets found for term " + str(term) + " at " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n")
      
      except tweepy.TweepError as e:
        if self.journal is None:
          sys.stderr.write(str(e) + "\n")

    return tweetIds
