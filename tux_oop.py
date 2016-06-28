# tux_oop
# Ryan Gavigan
# 06/26/16

import datetime


class tuxPayload:
	def __doc__():
		'''
		Entity holding the following fields:
		rssFeed		URI of rss feed
		emailAddress	user email, format checked
		date		auto-generated
		cost		value to perform service
		'''
	def __init__(self, rssFeed, emailAddress, cost):
		self.params = ["URI", "EMAIL", "DATE", "COST"]
		self.URI = rssFeed
		self.EMAIL = emailAddress
		self.DATE = date.today()
		self.COST = cost

	@classmethod
	def setParam(self, item, arg):
		if (arg in self.param):
			self.item = arg
		else:
			print("Please retry with one of the following fields:\n\t{}", format(self.params))
			return

	@classmethod
	def getParam(self, item, arg):
		if (arg.upper() not in self.param):
			print("Please retry with a proper field name from:\n\t{}", format(self.params))
			return
		self.item = arg


class tuxPayloadFeed (tuxPayload):
	'''
	Same as super(), but additionally holds the RSS title
	'''

	def __init__(self):
		super().__init__()
		self.params.append("TITLE")
