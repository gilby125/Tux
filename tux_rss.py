# tux_rss
# Ryan Gavigan
# 06/26/16

import feedparser
import tux_oop

'''
Get RSS feed then write the event status to the database
'''

def getTitle(uri):
	try:
		feed = feedparser.parse(uri)
		print("rss ln 15 %s", feed.get('title'))
	except feed.bozo_exception:
		print ("rss ln 15 "+ feed.bozo)
		return feed.bozo
	return feed.get('title')
