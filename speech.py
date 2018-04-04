# For Features
import os
import webbrowser as wb
from time import gmtime, strftime


# Plugin Based Archietecture
class Reply:
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


response['invalid'] = Reply('Sorry, I don\'t understand that yet!', None)
response['hello'] = Reply('Oh Hello There!', None)
response['browser'] = Reply('Opening google.com', browser)
response['what is the time'] = Reply(time, None)
response['what is the date'] = Reply(date, None)
response['quit'] = Reply('BBye!', quit)
