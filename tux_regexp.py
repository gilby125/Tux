# tux_regexp
# Ryan Gavigan
# 06/20/16
import re
import tux_oop
import tux_database

'''
Accept user input, populate tux entity and write the event status to database
'''


def UserInput():
	'''
	Accepts and checks user input for validity of email regex -- other fields are not checked
	'''
	rssFeed = input("Enter the URI of an rss feed:")
	while(True):
		emailAddress = input("Enter the designated email address:")
		regex = re.compile('[A-Z0-9._%+-]+@(?:[A-Z0-9-]+\.)+[A-Z]{2,6}')
		matchObj = re.search(regex, email)
		if(matchObj != None and matchObj.span()[1] == len(email)):
			print("Email address accepted!\n")
			break
		else:
			print("That's not a proper email address, please try again.\n")
	while(True):
		# Automatically generate datetime.date object with current date
		form = input('Enter a datetime format if you would like: \t')
		if(form != None):
			try:
				dt = datetime.date.__format__(form)
			except ValueError:
				dt = datetime.date.__format__(...)
				print('Incorrect format, using default (YYYY-MM-DD)')
				break
	while(True):
		cost = input("Enter a dollar amount: (ommitting $)")
		#  Assuming dollar ammount  < $1,000
		regex = re.compile('/?[0-9]{0,3}+?\.?[0-9]?[0-9]?/')
		matchObj = re.search(regex, cost)
		if(matchObj != None and matchObj.span()[1]):
			break
		else:
			print("This is not a correct dollar amount, please try again.\n")

	ret = [rssFeed,emailAddress,df,cost]
