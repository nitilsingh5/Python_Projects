import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(msg):
    engine.say(msg)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good Morning Boss!")
    elif(hour>=12 and hour<=18):
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")
    speak("I am your Assistent, How may I help you? ")

def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        r.energy_threshold=300
        audio = r.listen(source)
        query = r.recognize_google(audio,language="en-in")
        print("User Said:",query)
        return query

wishme()
while(1):
    if 1:
        query = takeComand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            query = query.replace("youtube", "")
            query = query.replace("search", "")
            webbrowser.open("https://www.youtube.com/results?search_query=" + query)
        elif 'facebook' in query:
            webbrowser.open("fb.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'google' in query:
            query = query.replace("google", "")
            query = query.replace("search", "")
            webbrowser.open("https://google.com/search?q=" + query)
        elif (('music' in query)or ('song' in query)):
            music_dir = 'G:/New folder/Music/English'
            songs = os.listdir(music_dir)
            rdm_song = random.choice(songs)
            os.startfile(music_dir+ '/' +rdm_song)
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("sir,the time is") 
            speak(time)
        elif 'sleep' in query:
            speak("Thank you Boss")
            exit() 
        