import requests
import pyttsx3
import json

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestNews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=d8c4451f499f4a8cbb0eccd3c8d4a964",
        "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=d8c4451f499f4a8cbb0eccd3c8d4a964",
        "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=d8c4451f499f4a8cbb0eccd3c8d4a964",
        "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=d8c4451f499f4a8cbb0eccd3c8d4a964"
    }
    content = None
    url = None
    speak("Which Field news you want,[Business, entertainment, sports, technology]")
    field = input("Type field you want")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url Not Found")

        news = requests.get(url).text
        news =json.loads(news)
        speak("Here is the first news")
        arts = news["articles"]
        for articles in arts:
            articles in articles["title"]
            print(articles)
            speak(articles)
            news_url = articles[news]
            print(f"for more info visit: {news_url}")
            a = input("[press 1 to continue ]and[ press 2 to stop]")
            if str(a) =="1":
                pass
            elif str(a) =="2":
                break


            speak("that's all")








