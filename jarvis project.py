import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
import time

TEMP_FILE = "temp_jarvis.mp3"  # Same file use karenge baar-baar

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save(TEMP_FILE)
    os.system(f'start {TEMP_FILE}') 
    time.sleep(1)  

def processcommands(c):
    print("Command:", c)
    if "youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif  "Link" in c.lower():
        webbrowser.open("https://www.linkdin.com/")
    elif  "insta" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif  "whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif  "ai" in c.lower():
        webbrowser.open("https://chatgpt.com/")
# This program for voice

if __name__ == "__main__":
    speak(" jarvis wake up")
    r = sr.Recognizer()

    while True:
        try:
            # Wake-word listening
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            print("Heard:", word)

            if "jarvis" in word.lower():
                speak("बोलो")
                print("Jarvis Active...")

                # Command listening
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Listening for command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                command = r.recognize_google(audio)
                processcommands(command)

        except Exception as e:
            print("Error:", e)