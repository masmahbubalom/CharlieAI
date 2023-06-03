import win32com.client
import os

# Set Your Name
name = "You"

# For Windows
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def say(text):
    s = text
    speaker.Speak(s)

# For macOS
# def say(text):
#     os.system(f"say {text}")


# todo: add OpenAI api key
apikey = "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"


# todo: add website name and url do you like
# like this - ['website name','url'] must use lower case

sites = [
    ['youtube', 'www.youtube.com'],
    ['google', 'www.google.com'],
    ['wikipedia', 'www.wikipedia.org'],
    ['facebook', 'www.facebook.com'],
    ['google drive', 'www.drive.google.com'],
    ['gmail', 'www.mail.google.com'],
    ['instagram', 'www.instagram.com'],
    ['twitter', 'www.twitter.com'],
    ['stack overflow', 'www.stackoverflow.com'],
    ['github', 'www.github.com']
]


# todo: add application name and path
# like this - ['app name','path'] must use lower case

apps = [
    ['calculator', 'C:\\Windows\\System32\\calc.exe'],
    ['firefox', 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'],
    ['cmd', 'cmd']
]
