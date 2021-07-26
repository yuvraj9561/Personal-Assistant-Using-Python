import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {name}")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon {name}")
    else:
        speak(f"Good evening {name}")
    speak("I'm your personal assistant Mr. Sky. How may I assist you?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")
            # text = r.recognize_google(audio)
            # print(text)
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"

        return query


def getName():
    r = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source, duration=1)
        # r.pause_threshold = 1
        # r.energy_threshold = 250
        # r.energy_threshold()
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            print('User said: ', text)
            return text
        except:
            print("sorry, could not recognise")


if __name__ == "__main__":
    # speak("Welcome Mr. Sky")

    speak("Hello Sir please enter your name?")
    # while True:
    #     print('Name: ', end=" ")
    #     name = input()
    #     print(f"Is your name {name}? Please say yes or no")
    #     speak(f"Is your name {name}? Please say yes or no")
    #     if 'yes' in getName().lower():
    #         print(f"Thanks for confirming your name {name}")
    #         speak(f"Thanks for confirming your name {name}")
    #         break
    #     else:
    #         print("Enter name again...")
    #         speak("Enter name again")

    print('Name: ', end=" ")
    name = input()
    wishMe(name)
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open('youtube.com')

        elif 'open google' in query:
            webbrowser.get(chrome_path).open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get(chrome_path).open('stackoverflow.com')

        elif 'open github' in query:
            webbrowser.get(chrome_path).open('github.com')

        elif 'open gfg' in query:
            webbrowser.get(chrome_path).open('https://www.geeksforgeeks.org')

        elif 'play music' in query or 'play song' in query:
            music_dir = 'D:\\SD RAHUl'
            songs = os.listdir(music_dir)
            # print(songs)
            song_no = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[song_no]))

        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")
        elif 'open vs code' in query or 'open visual studio code' in query:
            vs_path = "C:\\Users\\kambl\\AppData\\Local\\Programs\\Microsoft VS Code\\_\\Code.exe"
            os.startfile(vs_path)

        elif 'exit' in query or 'bye' in query:
            speak(f'Thank you {name} for for spending time with me')
            break

        elif 'thank you' in query or 'thanks' in query:
            speak("It's my pleasure")

        elif 'search' in query:
            a = query.replace('search', "")
            query = a.replace('google', "")
            webbrowser.get(chrome_path).open(
                f'https://www.google.com/search?q={query}')

        elif 'none' in query:
            speak("Speak again")
        elif 'you do' in query:
            string = "Opening youTube,Opening google,Opening stackoverflow,Opening gitHub,Opening gfg, Searching on Google,Searching on Wikipedia,Telling current time,Opening Visual studio code,playing music,"
            print(string.replace(',', "\n"))
            speak(string)
        else:
            webbrowser.get(chrome_path).open(
                f'https://www.google.com/search?q={query}')
