import tweepy
import json
import time
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

#define which tweet you want to trace all quote tweets for
startingTweet = '1261787165719232514'

searched = []

def search(id):
	global count, startTime, relationMap
	count += 1
	if (id not in searched):
		# search for tweets that quote the tweet with this `id` across twitter
		# we use the `url:` search operator with the tweet id as the search phrase 
		# since searching for entire tweet urls ("https://twitter.com/{user}/status/{id}")
		# was not returning all quote tweets
		searchResults = api.search('url:{}'.format(id), count=100)
		searched.append(id)
		print "{} quote tweets found for {}".format(str(len(searchResults)), id)
		for result in searchResults:
			print "http://www.twitter.com/{}/status/{}".format(result.user.screen_name, result.id_str)
			#Save file
			with open("tweets/{}.json".format(result.id_str), "w") as outfile: 
				outfile.write(json.dumps(result._json, indent=4))
			#avoid exceeding rate limit
			time.sleep(5)
			#find quote tweets for this result
			search(result.id_str)
	else:
		print "Key {} exists in `searched`".format(id)

#Save starting tweet
with open("tweets/{}.json".format(startingTweet), "w") as of: 
	of.write(json.dumps(api.get_status(startingTweet)._json, indent=4))

search(startingTweet)
	
