import datetime

import pyautogui
import pyttsx3
import requests
import speech_recognition
from bs4 import BeautifulSoup


for i in range(3):
    a = input("Enter Password to open assitant:")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("welcome ! please speak \"wake up\" to launch assistant")
        break
    elif i==2 and a!=pw:
        exit()
    elif a!=pw:
        print("try Agaain !")



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)

        try:
            print("Understanding...")
            query = r.recognize_google(audio,language='en-in')
            print(f"Your Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query
if __name__ =="__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
#####################################################
        elif "change password" in query:
            speak("whats the new password!")
            new_pw = input("Enter New password: ")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("done sir!")
            speak(f"your news password is {new_pw}")

            #####################################################
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("OK sir, You can call me anytime")
                    break
                elif "hello" in query:
                    speak("Hello Sir, How are you ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("perfect sir")
                elif "thank you" in query:
                    speak("your welcome, sir")

                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)
                elif "news" in query:
                    from newsRead import latestNews
                    latestNews()

                elif "temperature" in query:
                    search = "temperature in Indore"
                    url= f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "weather" in query:
                    search = "temperature in Indore"
                    url= f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "time" in query:
                    # search = "Current time is "
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {strTime}")
                elif "shut down" in query:
                    speak("going to sleep, sir")
                    exit()

                elif "open" in query:
                    from Dictapp import openAppWeb
                    openAppWeb(query)
                elif "close" in query:
                    from Dictapp import closeAppWeb
                    closeAppWeb(query)


#                 youtbe
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video pause")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video play")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video Unmuted")
                elif "volume up" in query:
                    from keyboard import volumeUp
                    volumeUp()
                    speak("Volume Up!")
                elif "volume down" in query:
                    from keyboard import volumeDown
                    volumeDown()
                    speak("Volume Down!")

