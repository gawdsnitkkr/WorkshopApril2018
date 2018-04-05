# For Features
import os
import urllib
import webbrowser as wb
import subprocess
from time import gmtime, strftime


# Plugin Based Architecture
class Reply:
    # text can be a text generating function or a string
    # action can be None or a function to perform action
    def __init__(self, text, action):
        self.__text = text
        self.__action = action

    def getReply(self, text):
        return self.__text(text) if callable(self.__text) else self.__text

    def action(self, text):
        if self.__action and callable(self.__action):
            self.__action(text)


response = {}


def browser(text):
    wb.open('http://google.co.in', new=2)


def time(text):
    return strftime("It\'s %I:%M %p", gmtime())


def date(text):
    return strftime("Today is %d-%B-%Y", gmtime())


def quit(text):
    os._exit(0)


def search(text):
    query = text
    url = 'https://www.google.co.in/search?q=' + urllib.parse.quote_plus(query)
    wb.open(url, new=2)


def define(text):
    query = 'define ' + text
    search(query)

def shutdown(text):
    if os.name == 'nt': # for windows
        os.system("shutdown -s")
    else: # linux
        os.system("poweroff")

def music(text):
    if os.name == 'nt': # for windows
        # os.system("wmplayer") # not tested yet 
        os.system("vlc")# for windows working
    else: # linux
        os.system("rhythmbox")

def openExplorer(text):
    subprocess.call('explorer')


response['invalid'] = Reply('Sorry, I don\'t understand that yet!', None)
response['hello'] = Reply('Oh Hello There!', None)
response['browser'] = Reply('Opening google.com', browser)
response['what is the time'] = Reply(time, None)
response['what is the date'] = Reply(date, None)
response['quit'] = Reply('BBye!', quit)
response['shutdown'] = Reply("Shutting down...",shutdown)
response['play music'] = Reply("Playing your music!!", music)

# Features to read info after a command word
response['define'] = Reply('', define)
response['search'] = Reply('', search)
response['open my computer'] = Reply('', openExplorer)
response['open this p c'] = Reply('', openExplorer)
response['open this pc'] = Reply('', openExplorer)
response['open explorer'] = Reply('', openExplorer)