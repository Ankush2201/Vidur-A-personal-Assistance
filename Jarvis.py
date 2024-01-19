import pyttsx3
import datetime as datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os as o
import smtplib # for Emaling purpose




engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def greeting() :
    greet= "Hello , I am Chanakya "
    speak(greet)


def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12 :
       wishtext = f" Good Morning Boss , Now its{datetime.datetime.now().hour} {datetime.datetime.now().minute} am "
    elif hour >=12 and hour < 16 :
        wishtext = f" Good afterNoon Boss , Now its {datetime.datetime.now().hour} {datetime.datetime.now().minute}  pm " 
    elif hour >= 16 and hour <=24  :
        wishtext = f"Good Evening Boss , Now its {datetime.datetime.now().hour} {datetime.datetime.now().minute} pm"
    speak(wishtext)

def TakeInput():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening......")
        r.pause_threshold = 0.8
        r.energy_threshold = 200
        audio = r.listen(source)
    
    try : 
        print("Recognizing ... ")
        spoke= r.recognize_google(audio, language="en-US")
        print(f"user said : {spoke}")
    except Exception as e :
        print("Can't Understand Query ..")
        speak("Can You say That again Boss")
        return 'None' 
    return spoke 
    

def Wikipedia(query):
    query=query.replace("wikipidea" , " ")
    results = wikipedia.summary(query , sentenses=2)
    speak("According to WikiPedia...")
    print(results)
    speak(results)

def repeat():
    speak("ok i will do ...Tell me what to do")
    while True:
        query_re = TakeInput().lower()
        speak(query_re)
        if 'quit repeat' in query_re:
            speak('Ok Boss !!!!!!')
            break 

def VS_code():
    codepath= "C:\\Users\\aayushi pandey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #openlocation->property->target_location
    o.startfile(codepath)

def brave():
    bravepath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" # " \\ " imp to add
    o.startfile(bravepath)

def openmyfolder():
    my_dir = 'C:\\Users\\Ankush_folder'
    files = o.listdir(my_dir)
    print(files)
    o.startfile(my_dir)

if __name__ =="__main__" :
    greeting()
    while True :
        query=TakeInput().lower()

        if 'wikipedia' in query:
            Wikipedia(query)
        elif 'wish me' in query :
            wishMe()
        elif 'repeat after me' in query:
            repeat()
        elif 'open youtube' in query :
            webbrowser.open('youtube.com')
        elif 'open Google' in query :
            webbrowser.open('google.com')
        elif 'open chat gpt' in query :
            webbrowser.open('chat.openai.com')
        elif 'open my folder' in query :
            openmyfolder()
        elif 'open code' in query :
            VS_code()
        elif 'open brave' in query :
            brave()
        elif 'quit' in query :
            speak("OK Boss Quiting..have a Good Instance")
            break
