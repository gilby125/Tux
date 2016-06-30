# tux_rss
# Ryan Gavigan
# 06/29/16

import feedparser
import tux_oop

'''
Get RSS feed then write the event status to the database
'''


def getTitle(uri):
	try:
		feed = feedparser.parse(uri)
	except feed.bozo_exception:
            insertEvent('Events', 'RF')		
            return feed.bozo
	return feed.get('title')
