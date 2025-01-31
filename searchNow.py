import webbrowser

import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)
        try:
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Your Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
query = takeCommand().lower()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("this is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")


def searchYoutube(query):
    if "youtube" in query:
        query = query.replace("jarvis", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        speak("this is what i found on youtube search")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("searching on wikipedia")
        query = query.replace("jarvis", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("wikipedia", "")
        speak("this is what i found on wikipedia search")
        results =wikipedia.summary(query,sentences =2)
        speak("According to wikipedia...")
        print(results)
        speak(results)























