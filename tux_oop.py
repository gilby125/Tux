#!/bin/python


# entity module that contains the class tuxPayload data members
# and method members. Inherit the tuxPayload in a class called
# tuxPayloadFeed - add a data member to hold the feed title.


class tuxPayload:
	def __init__(self):
		print("Created a new tuxPayload object")
	def setURI(self, arg):
		self.uri = arg


class tuxPayloadFeed (tuxPayload):
	def __init__(self, title):
		self.title = title
		print("New tuxPayloadFeed object title is:",self.title)

	def setTitle(self, arg):
		self.title = arg

	def getTitle(self):
		print("Feed title is:",self.title)
 
