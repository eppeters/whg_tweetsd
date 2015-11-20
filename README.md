# whg_tweetsd
A Twitter bot that retweets about Wheeling, WV. It is best run as a daemon.

# Sensitive data in the history
Let's get the elephant out of the room.

I had not planned on making whg_tweetsd public, but now I have.

One of the consequences of my original plan (or lack thereof) was that I left the bot's Twitter API secrets in the code, and committed them.

Rest assured, I know it would be bad to make those public, so I have regenerated the live version's API secrets and abstracted out the secrets into the config file so that, if you want, you can replace them.

In short, the keys in the history will not work as of this repository going public.

# What it is
Wheeling Tweets (or, formally, whg_tweetsd) retweets things people say about Wheeling, WV around the city. It's my hometown, and there's a lot of good culture there. It needed some attention, and a cool, centralized place for people to see buzz about the city.

It uses keywords that only people in Wheeling would know to find tweets at various distances from Wheeling Jesuit University (the current basis of all searches), depending on how global those search terms are.

(For instance, "Dicarlo's Pizza" would probably go a ways before it meets another Dicarlo's, but there's a Wheeling, Illinois, so "Wheeling" won't quite do it. Also there's the whole "four-wheeling" thing.

# Live Version
The bot is live and can be seen controlling [this Twitter account](https://twitter.com/wheeling_tweets)
