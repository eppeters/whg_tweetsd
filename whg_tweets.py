import tweepy
from time import sleep

### Twitter authorization
auth = tweepy.OAuthHandler('GW6ygIXuDjY09UysWCWwl3SYz', 'GtidKGLHvMAXMEs2p7Vict6HE4Z2p7gAnS2P7BQisEqNYa7kuC')
auth.set_access_token('2847055289-pn4f6qKRV2OWUoQIjyBJZu0GUyd5w0D13OB1Bl5', 'hZWi3AHudKgFrLFJ8a9dgL12ds5Bvpt6zh9ZBHvcUdBzR')

### Configuration
interval_secs = 60 * 30 # 30 minutes
wju = '40.069562,-80.69173' # Wheeling Jesuit University's long/lat
distance = '60mi' # roughly to Pittsburgh
geo = wju + ',' + distance
last_checked_id = 526379098805768194
keyword = 'wheeling, wv'
lang = 'en'

twitter = tweepy.API(auth)

while True:
	posts = []
	try:
		if (last_checked_id != None):
			print "LAST_CHECKED_ID: last_checked_id = ", last_checked_id
			posts = twitter.search(keyword, lang,
					since_id = last_checked_id, geocode = geo)
		else:
			posts = twitter.search(keyword, lang, geocode = geo)
	except tweepy.TweepError as e:
		print e

	for post in posts:
		try:
			result = twitter.retweet(post.id)
			print "RESULT: ", result
		except tweepy.TweepError as e:
			print "ERROR: ", e
			print "ERROR: Next post is the error'd one."
		print "POST INFORMATION: id = ", post.id, "text = ", post.text.encode('utf8')
		print "POST INFORMATION: ", post
		last_checked_id = post.id
		print "LAST_CHECKED_ID: last_checked_id = ", last_checked_id

	print "SLEEP: Sleeping for ", interval_secs, " seconds"
	#sleep(interval_secs)
	print "SLEEP: Finished sleeping. Restarting search."
