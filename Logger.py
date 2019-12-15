from datetime import datetime
import re
import MySQL


# Error = when the approximate location of the crash is known
def LogError(error):
    f = open("Log.txt", "a")
    f.write("\n" + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " ERROR: " + error)
    f.close()


# NOTE = when the data inseredted in db is as good as its going to get
def LogNote(note):
    f = open("Log.txt", "a")
    f.write("\n" + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " Note: " + note)
    f.close()


# Crash = Catchall for the entire scrape
def LogCrash(error):
    f = open("Log.txt", "a")
    f.write("\n" + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " CRASH: " + error)
    f.close()


def recycle_Urls():
    f = open("Log.txt", "r")
    for l in f:
        url = re.search("https.+?.html", l)
        if url:
            MySQL.populate_table("urlstoscrape", ("url", url[0]))
