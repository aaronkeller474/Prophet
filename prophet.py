import speech_recognition as sr
from os import system
import webbrowser as wb


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    system('say Hello. How may I assist you?')
    audio = r.listen(source)

def Firefox():
    wb.open('http://www.google.com')

def Facebook():
    wb.open('http://www.facebook.com')

def Gmail():
    wb.open('http://www.gmail.com')

def Youtube():
    wb.open('http://www.youtube.com')

try:
    text = r.recognize_google(audio)
    # system('say Did you say ' + text) # Testing Purposes
    print(text) # Makes sure correct names are entered
    if text == 'hello':
        system('say Hello! How are you today?')
    elif text == 'Firefox':
        system('say Opening Firefox')
        Firefox()
    elif text == 'Facebook':
        system('say Opening Facebook')
        Facebook()
    elif text == 'Gmail':
        system('say Opening Gmail')
        Gmail()
    elif text == 'YouTube':
        system('say Opening Youtube')
        Youtube()
    else:
        system('say I didn\'t understand what you said. Can you please repeat it!!')

except:
    pass



if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
