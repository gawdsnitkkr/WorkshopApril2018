
import pyttsx3 as tts  # For Text to Speech
import speech_recognition as stt  # For Speech to Text

from app.speech import response  # For Features

from app.config import tts_config
from app.config import stt_config

import app.log as app_logger
logger = app_logger.setup_custom_logger('root')

def start_app():

    # Initialize Text To Speech(TTS)
    engine = tts.init()
    engine.setProperty('rate', tts_config['rate'])

    # Initialize Speech To Text(STT)
    sample_rate = stt_config['sample_rate']
    chunk_size = stt_config['chunk_size']  # buffer size
    recognizer = stt.Recognizer()  # init recognizer
    language = stt_config['language']  # for text to speech language
    device_id = 0  # first device (microphone)

    # Get Microphone Device ID
    logger.info('Available Audio Devices: ')
    mic_list = stt.Microphone.list_microphone_names()
    for i, micName in enumerate(mic_list):
        print(i, micName)

    try:
        device_id = int(input('Microphone ID: '))
    except Exception as e:
        logger.error('Invalid Driver ID, using 0')
    finally:
        device_id = 0 if device_id < 0 or device_id >= len(mic_list) else device_id

    try:
        with stt.Microphone(device_index=device_id, sample_rate=sample_rate, chunk_size=chunk_size) as source:
            recognizer.adjust_for_ambient_noise(source)  # removing noise
            logger.info("Ready.")

            while True:  # STT Loop
                audio = recognizer.listen(source)  # listen from mic

                try:
                    text = recognizer.recognize_google(audio)  # recognize with google
                    logger.info("You said:")
                    logger.info(text)
                    text = text.lower()

                    # Fetch Reply
                    reply = None
                    if text in response:
                        reply = response[text]
                    else:
                        tokens = text.split()
                        if len(tokens) > 0 and tokens[0] in response:
                            reply = response[tokens[0]]
                            text = text[len(tokens[0]) + 1:]
                        else:
                            reply = response['invalid']

                    reply.action(text)  # Perform Action

                    output = reply.getReply(text)  # Generate Reply
                    logger.info(output) #logger Reply
                    engine.say(output)  # TTS
                    engine.runAndWait()  # Wait for Speech To Complete

                except stt.UnknownValueError as e:
                    logger.error("Google Speech Recognition could not understand audio")
                except stt.RequestError as e:
                    logger.error("Could not request results from Google Speech Recognition service; {0}".format(e))
                except Exception as e:
                   logger.warn(e)

    except Exception as e:
        logger.warn("Exception Occurred")
        logger.warn(e)
