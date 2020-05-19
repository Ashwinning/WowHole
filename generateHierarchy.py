import json
from os import listdir
from os.path import isfile, join
import csv


'''
with open('relationMap.json', 'r') as f:
	json.load(f)
'''
mypath = 'tweets'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

headings = ['id','name','handle','tweet','refs','url','image']

c = open('data.csv', 'w')
writer = csv.writer(c)
writer.writerow(headings)

for doc in onlyfiles:
	with open('tweets/'+doc, 'r') as f:
		data = json.load(f)
		print '{} | {}'.format(data['user']['screen_name'], doc)
		content = []
		content.append(data['id_str'])
		content.append(data['user']['name'])
		content.append(data['user']['screen_name'])
		content.append(unicode(data['text']).encode("ascii", 'ignore').replace(",", '').replace('\n', ' '))
		if ('quoted_status' in data.keys()):
			content.append(data['quoted_status']['id_str'])
		else:
			content.append(data['retweeted_status']['id_str'])
		content.append('https://twitter.com/{}/status/{}'.format(data['user']['screen_name'], data['id_str']))
		content.append(data['user']['profile_image_url'])
		print content
		writer.writerow([unicode(s).encode("utf-8") for s in content])
