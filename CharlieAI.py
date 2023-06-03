import os.path
import speech_recognition as sr
import webbrowser
import openai
from config import apikey, sites, apps, name, say, speaker
import datetime
import wikipedia


# Function Area

# Chat with AI
chatStr = ""
def chat(quary):
    global chatStr
    openai.api_key = apikey
    chatStr += f"{name} : {quary}\n Charlie : "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        say(response["choices"][0]["text"])
    except:
        pass
    chatStr += f'{response["choices"][0]["text"]}\n'
    return response["choices"][0]["text"]

# Open Website
def openWebsite(siteName):
    url = f"https://www.{siteName}"
    say(f'opening {siteName}')
    webbrowser.open(url)

# Open YouTube Channel
def openYoutubeChannel(channelName):
    say(f'opening {channelName} youtube channel')
    url = f"https://www.youtube.com/@{channelName}"
    webbrowser.open(url)

# Audio Capture
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en')
            print(f'{name} : {query}')
            return query.lower()
        except:
            return ""


# Main Area

def TaskExecution():
    hlw = "Hi I'm Charlie. How can I help you?"
    speaker.Speak(hlw)

    while True:
        print('Listening...')
        quary = takecommand()

        # Open Listed Website
        for site in sites:
            if f'open {site[0]}' in quary:
                say(f'opening {site[0]}')
                webbrowser.open(site[1])

        # Open Listed app
        for app in apps:
            if f'open {app[0]}' in quary:
                say(f'opening {app[0]}')
                os.startfile(app[1])

        # Time
        if "the time" in quary:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            say(time)
        elif "today date" in quary:
            date = datetime.date.today().strftime("%d/%m/%Y")
            say(date)

        #Open Any Website
        elif 'open' in quary and 'website' in quary:
            QuaryOne = quary.replace("open", "").strip()
            QuaryTwo = QuaryOne.replace("website", "").strip()
            siteName = QuaryTwo.replace(" ", "").strip()
            openWebsite(siteName)

        # Open Any YouTube Channel
        elif "youtube channel" in quary:
            newQuary = quary.replace("open", "").strip()
            newQuaryTwo = newQuary.replace("youtube channel", "").strip()
            channelName = newQuaryTwo.replace(" ", "").strip()
            openYoutubeChannel(channelName)

        # Wikipedia
        elif "according to wikipedia" in quary:
            say("Searching Wikipedia...")
            quary = quary.replace("wikipedia","")
            result = wikipedia.summary(quary,sentences=3)
            say(f"according to wikipedia {result}")


        elif "made you" in quary or "create you" in quary:
            say("I am an AI assistant created by Mahbub Alam")
        elif "your parents" in quary:
            say("My parents name is Mahbub Alam")
        elif "develop you" in quary or "your developer" in quary:
            say("My Developer name is Mahbub Alam")
        elif "mahbub alam" in quary or "mahbub" in quary or "mahbub alom" in quary:
            say("Mahbub Alam is a Machine Learning Engineer. He created me. Find him by username m a s m a h b u b a l o m")


        elif "reset chat" in quary:
            chatStr = ""
        elif "charlie quit" in quary or "bye" in quary:
            say("ok, bye")
            exit()

        else:
            print("Chatting...")
            chat(quary)

TaskExecution()
# The End