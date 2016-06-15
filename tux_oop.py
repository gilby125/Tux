# entity module that contains the class tuxPayload data members
# and method members. Inherit the tuxPayload in a class called
# tuxPayloadFeed - add a data member to hold the feed title.
import date


class tuxPayload:

    def __init__(self, rssFeed, emailAddress):
        self.Date = date.today()
        self.params = ["URI", "EMAIL", "DATE", "COST"]
        self.rssFeed = rssFeed
        self.emailAddresss = emailAddress
        print("Created a new tuxPayload object")

    def setParam(self, item, arg):
        if(arg not in self.param):
            self.item = arg
        else:
            print("Please retry with a proper field name from:\n\t", self.params)
            return

    def getParam(self, item, arg):
        if(arg.upper() not in self.param):
            print("Please retry with a proper field name from:\n\t", self.params)
            return
        self.item = arg


class tuxPayloadFeed (tuxPayload):

    def __init__(self, title):
        self.params.append("TITLE")
        self.title = title
        print("New tuxPayloadFeed object title is:", self.title)
