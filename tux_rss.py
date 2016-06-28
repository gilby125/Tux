# tux_rss
# Ryan Gavigan
# 06/26/16

import feedparser
import tux_oop
import tux_database

'''
Get RSS feed then write the event status to the database
'''


def getTitle(uri):
	try:
		feed = feedparser.parse(uri)
	except feed.bozo_exception:
		insertEvent('RF')
		return feed.bozo
	try:
		title = feed.pop('title')
		insertEvent('RO')
		return title
	except KeyError:
		return insertEvent('RF')
