import pyttsx3
import speech_recognition as sr
# import webbrowser
import datetime
import pyjokes
import os
import openai
import time


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try :
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError :
            print("Not recognizing.")
def speechtx():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 175)
    engine.say(x)
    engine.runAndWait()
speechtx()

if __name__=='__main__':
    if sptext().lower() == "Hey, Peter" :
        while True :
                data1 = sptext().lower()
                if "Your Name : " in data1:
                    name = "My name is Peter "
                    speechtx(name)
                elif "Old are you" in data1:
                    age = "i am Two Years OlD "
                    speechtx(age)
                elif "Now Time" in data1:
                    time = datetime.datetime().now().strftime("%I%M%p")
                    speechtx(time)
                elif "Youtube" in data1:
                    webbrowser.open("https://www.youtube.com/")
                elif "Facebook" in data1:
                    webbrowser.open("https://www.facebook.com/")
                elif "todaynews" in data1:
                    webbrowser.open("https://www.todaynews.com/")
                elif "in google" in data1:
                    webbrowser.open("https://www.google.com/")
                elif "Joke" in data1:
                    Joke_1 = pyjokes.get_joke(language="en",category="netrual")
                    print(Joke_1)
                    speechtx(Joke_1)
                # elif "Play Song" in data1 :
                #     addr= "Location play list"
                #     listsong = os.listdir(addr)
                #     print(listsong)
                #     os.startfile(os.path.join(addr,listsong[0]))
                    # song = playsound.play("PlayListLocation")
                    # speechtx(song)
                elif "exit" in data1:
                    speechtx("Thank you !")
                    break

                time.sleep(5)

else :
    print("Thank you!")

    
              