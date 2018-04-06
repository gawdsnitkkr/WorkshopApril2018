# For Features
import os
import urllib
import webbrowser as wb
import subprocess
import ctypes
from time import gmtime, strftime
import pyautogui
import uuid
import requests

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
        os.system("vlc")
        # os.system("wmplayer")
    else: # linux
        os.system("rhythmbox")

def openExplorer(text):
    subprocess.call('explorer')

def lock(text):
    if os.name == 'nt':
        ctypes.windll.user32.LockWorkStation()
    else:
        os.popen('gnome-screensaver-command --lock')

def screenshot(text):
    x=uuid.uuid4()
    pyautogui.screenshot('/download/img'+str(x)+'.png')

def weather(text):
    city_id = 2172797
    req = requests.get('http://samples.openweathermap.org/data/2.5/weather?id='+str(city_id)+'&appid=8a525710a52517509ce8c40c4c42b04a')
    json_object = req.json()
    temp_k = float(json_object['main']['temp'])
    temp = (temp_k - 273.15) * 1.8 + 32
    s = 'The temperature is '+str(temp)+' Farenheit'
    return s

response['invalid'] = Reply('Sorry, I don\'t understand that yet!', None)
response['hello'] = Reply('Oh Hello There!', None)
response['browser'] = Reply('Opening google.com', browser)
response['what is the time'] = Reply(time, None)
response['what is the date'] = Reply(date, None)
response['quit'] = Reply('BBye!', quit)
response['shutdown'] = Reply("Shutting down...", shutdown)
response['play music'] = Reply("Opening music player...", music)
response['lock'] = Reply("Locking your computer", lock)
response['screenshot'] = Reply('Taking screenshot',screenshot)
response['weather'] = Reply(weather,None)

# Features to read info after a command word
response['define'] = Reply('', define)
response['search'] = Reply('', search)
response['open my computer'] = Reply('', openExplorer)
response['open this p c'] = Reply('', openExplorer)
response['open this pc'] = Reply('', openExplorer)
response['open explorer'] = Reply('', openExplorer)