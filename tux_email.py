import smtplib
from email.mime.text import MIMEText


def tuxEmail:
    '''
    Email the user the RSS title & write event status to database
    '''
    def __init__(self, emailAddress, rssTitle):
        self.emailAddress = emailAddress
        self.rssTitle = rssTitle
    
    def sendEmail(self, emailAddress):
