# tux_rss
# Ryan Gavigan
# 06/20/16

import feedparser

'''
Get RSS feed then write the event status to the database
'''

python_wiki_rss_url = "http://www.python.org/cgi-bin/moinmoin/" \
    "RecentChanges?action=rss_rc"

feed = feedparser.parse(python_wiki_rss_url)

print feed["url"]
