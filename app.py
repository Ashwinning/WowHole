import tweepy
import json
import time
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

#print json.dumps(api.retweets('1261855313705095168')[0]._json, indent=4)

# the retweets API does not return quote tweets
'''
rts = api.retweets('1261858289383440384')
for rt in rts:
	print json.dumps(rt._json, indent=4)
'''

count = 0

#define which tweet you want to trace all quote tweets for
startingTweet = '1261787165719232514'

startTime = time.clock()
print startTime
print count

relationMap = {}
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
			#Add to RelationMap
			relationMap[result.id_str] = {
				'screen_name': result.user.screen_name,
				'id': result.id_str,
				'parent': id
			}
			print "http://www.twitter.com/{}/status/{}".format(result.user.screen_name, result.id_str)
			#Save relationMap
			with open('relationMap.json', 'w') as fp:
				json.dump(relationMap, fp, indent=4)
			with open('searched.json', 'w') as fp:
				json.dump(searched, fp, indent=4)
			#Save file
			with open("tweets/{}.json".format(result.id_str), "w") as outfile: 
				outfile.write(json.dumps(result._json, indent=4))
			'''
			#if rate limit has exceeded
			if (time.clock()-startTime) > (15 * 60) or count > 179:
				waitTime = (15 * 60)-(time.clock() - startTime) + 5
				print "Rate limit exceeded, waiting for {} seconds".format(str(waitTime))
				#wait till the 15 min period is over
				time.sleep(waitTime)
				#reset count and time
				count = 0
				startTime = time.clock()
			'''
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
	
