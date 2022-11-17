# import imp
import importlib
from pip import main
import wikipedia
import pyttsx3
import datetime
import webbrowser
import os
import random
# import pyaudio
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening..........")
        # speak("yess i can hear you.......")



        # print("Say something!")
        # audio = r.listen(source,timeout=1,phrase_time_limit=10)

        # r.pause_threshold = 1
        # r.energy_threshold = 100
        
        audio= r.listen(source)
        

    try:
        print("Recognizing......")
        query = r.recognize_google(audio , language= 'hindi')
        print(f"user said: {query}\n" )
        # speak(query)

    except Exception as e:
        print(e)
        # print("Say that again Please....")
        # speak("Say that again Please....")
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon Sir!")
    else:
        print("Good Evening sir! ")
        speak("Good Evening sir! ")
        
    speak("I am Jarvis , Please tell me how may I help you")

if __name__ == "__main__":
    # speak("Raj is a good boy!")

    wishMe()

    while True:
    
        query = takeCommand().lower()
        if "wikipedia" in query:
            query = query .replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("Searching wikipedia...")

            speak("According to wikipedia..")
            # print(results)``
            speak(results)


        elif "music" in query:
            music_dir = "H:\\Chill & Lofi Songs\\mobile songs"
            songs = os.listdir(music_dir)
            num= random.randrange((len(songs)-1))
            # print(num)
            print(songs[num])

            # str1 = ""
 
    
            # for ele in songs:
                # str1 += ele
            
            # print(str1.encode("utf-8"))
            os.startfile(os.path.join(music_dir, songs[num]))


        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime) 
            speak(f"Sir, The time is {strtime}")

        elif "repeat" in query:
            speak(query)
                       

