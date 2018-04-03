import speech_recognition as sr # for speech to text
from gtts import gTTS # for text to speech
import subprocess # required for play audio
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 120)

mic_name = "HDA Intel PCH: ALC3234 Analog (hw:0,0)" # microphon hardware id
sample_rate = 48000     # often values are recorded
chunk_size = 2048       # buffer size
r = sr.Recognizer()     # init recognizer
language = 'en'         # for text to speech language
device_id = 0           #first device (microphon)

mic_list = sr.Microphone.list_microphone_names() # get all microphon name
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i # set the mic id which I want to use

questions = ['how are you' , "hello"]
answer = ['I am fine sir, thank you' , "hello Sir,I am your Laptop,How can I help you,sir"]

def start():
    with sr.Microphone(device_index=device_id, sample_rate=sample_rate,chunk_size=chunk_size) as source:
        r.adjust_for_ambient_noise(source) # removing noise
        print("Start..........")
        audio = r.listen(source)# listen from mic
        try:
            text = r.recognize_google(audio) # recognize with google
            print("You said: " + text)
            text = text.lower()
            reply = ""
            if text in questions:
                reply = answer[questions.index(text)]
            else:
                reply = "I did not get you, better luck next time"

            engine.say(reply)
            engine.runAndWait()
            # myobj = gTTS(text=reply, lang=language, slow=False)
            # myobj.save("nk.amr")
            # subprocess.call(["ffplay", "-nodisp", "-autoexit", "nk.amr"])
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google  Speech Recognition service; {0}".format(e))
start()