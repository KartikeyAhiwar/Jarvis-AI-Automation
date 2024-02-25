import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
# import random
from requests import get
import wikipedia
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)


# 1) For Text to Speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# 2) For Voice to Text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(sourse, timeout=2, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en_in')
        print(f"user said: {query}")


    except Exception:
        speak("Say that again please...")
        return "none"
    return query  #


# 3) To show Current Date & Time wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("i am jarvis please tell me ,how can i help you")


# Func to send Email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kartikeyahirwar3@gmail.com', 'kartik20@')
    server.sendmail('kartikeyahirwar3@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:
        if 1:
            query = takecommand().lower()

            # 4) To open the notepad
            # logic building for task
            if "open notepad" in query:
                npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2312.18.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
                os.startfile(npath)

            # 5) To open the command prompt
            elif "open command prompt" in query:
                os.system("start cmd")

            # 6) To open the Camera
            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            # 7) To play music
            elif "play music" in query:
                music_dir = "C:\\Users\\asus\\Desktop\\windows.mp3"
                songs = os.system(music_dir)
                os.startfile(os.path.join(music_dir, songs))
            # rd = random.choice(songs)
            # for song in songs:
            # if songs.endswith('.mp3'):
            # os.startfile(os.path.join(music_dir,song))

            # 8)--> To check IP address

            elif "what is my Ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"Sir,Your IP address is{ip}")

            # 9)--> To searching from wikipedia through cammand
            elif "wikipedia" in query:
                speak("search wikipedia....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentence=2)
                speak("according to wikipedia")
                speak(results)
                print(results)

            # 10) To open the YouTube
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            # 11) To open the Google & search also
            elif "open google" in query:
                speak("sir, what should i search in google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")

            # 12) To sending the message in whatup
            elif "send message" in query:
                kit.sendwhatmsg("+917225863407", "this testing of Javis automation project", 0, 1)

            #  or
            # cm = takecommand().lower()
            # speak("sir,Who do you want to send the message to?")
            # kit.sendwhatmsg("+917225863407",f"{cm}",0,2,25)
            # 13) To play video / song
            elif "play songs on youtube" in query:
                kit.playonyt("labon pe")

            # 14)--> To send email to any one
            elif "send email to me" in query:
                try:
                    speak("what should i send?")
                    content = takecommand().lower()
                    to = ' kartikeyahirwar3@gmail.com '
                    sendEmail(to, content)
                    speak("Email has sent to you")
                except Exception as e:
                    print("sorry sir, i am not able to solve this email")

            # 15) bye bye javis
            elif "no" in query:
                speak("thankyou for using jarvis sir ,have a good day")
                sys.exit()
            speak("sir, do you have any other work")
