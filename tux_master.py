# tux_master
# Ryan Gavigan
# 06/26/16
import tux_regexp
import tux_database
import tux_email
import tux_rss
import tux_oop
import subprocess

subprocess.call('clear', shell=True)

tuxPF = tux_regexp.UserInput()

print ("Feed URI: %s", tuxPF['URI'])
print ("Feed title: %s", tuxPF['TITLE'])
print ("Email address: %s", + tuxPF['EMAIL'])
print ("Date: %s", tuxPF['DATE'])

# Order of processes:
# Process1:(tux_regexp.py) accept user input and populate the tux entity and
    # write the event status to the database.
# Process2:(tux_rss.py) try and get the RSS feed & write event status to db
# Process3:(tux_email.py) email user the RSS title & write event status to db.
# Process4: read the database status events and print them out to the screen.
