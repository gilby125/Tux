# tux_regexp
# Ryan Gavigan
# 06/26/16
import re
import tux_oop
import tux_database
import tux_rss


def UserInput():
	'''
	Accepts and checks user input for validity of email regex -- other fields are not checked
	'''
	uri = input("Enter the URI of an rss feed: ")
	title = tux_rss.getTitle(uri)
	while(True):
		email = input("Enter the designated email address: ")
		regex = re.compile('[A-Z0-9._%+-]+@([A-Z0-9-]?+\.)+[A-Z]{2,6}')
		matchObj = re.search(regex, email)
		if(matchObj is not None and matchObj.span()[1] == len(email)):
			print("Email address accepted!\n")
			break
		else:
			print(matchObj)
			print("That's not a proper email address, please try again. '%s'\n", email)
	while(True):
		# Automatically generate datetime.date object with current date
		form = input('Enter a datetime format if you would like: ')
		if(form is not None):
			try:
				dt = datetime.date.__format__(form)
			except ValueError:
				dt = datetime.date.__format__(...)
				print "Incorrect format, using default (YYYY-MM-DD)"
				break
	while(True):
		cost = input("Enter a dollar amount: (ommitting $) ")
		#  Assuming dollar ammount  < $1,000
		regex = re.compile('/?[0-9]{0,3}+?\.?[0-9]?[0-9]?/')
		matchObj = re.search(regex, cost)
		if(matchObj is not None and matchObj.span()[1]):
			break
		else:
			print "This is not a correct dollar amount, please try again.\n"
	ret = tuxPayloadFeed.__init__(rssFeed, emailAddress, df, cost)
	ret.setParam('TITLE', title)
	return ret
