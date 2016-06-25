# tux_rss
# Ryan Gavigan
# 06/20/16

import feedparser
import tux_oop

'''
Get RSS feed then write the event status to the database
'''

def getTitle(uri):
	try:
		feed = feedparser.parse(uri)
		print(feed['title'])
	except feed.bozo_exception:
		print (feed.bozo)
		return feed.bozo
	return feed['feed']['title']
