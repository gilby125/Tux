# entity module that contains the class tuxPayload data members
# and method members. Inherit the tuxPayload in a class called
# tuxPayloadFeed - add a data member to hold the feed title.


class tuxPayload:
	self.params = ["URI", "EMAIL", "DATE", "COST"]
	def __init__(self, rssFeed, emailAddress):
		#self.Date = 
		self.rssFeed = rssFeed
		self.emailAddresss = emailAddress
		print("Created a new tuxPayload object")
	def setParam(self, item, arg):
		if(!(arg in self.param)):
			self.item = arg
		else:
			print("Please retry with a proper field name from:\n\t",self.params)
			return
	def getParam(self, item, arg):
		if(!(arg.upper() in self.param)):
			print("Please retry with a proper field name from:\n\t",self.params)
			return
		self.item = arg


class tuxPayloadFeed (tuxPayload):
	self.params.append("TITLE")
	def __init__(self, title):
		self.title = title
		print("New tuxPayloadFeed object title is:",self.title)
 
