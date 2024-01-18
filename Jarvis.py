import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia




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
    elif hour >= 4 and hour < 0 :
        wishtext = f"Good Evenng Boss , Now its {datetime.datetime.now().hour} {datetime.datetime.now().minute} pm"
    speak(wishtext)

def TakeInput():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 100
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
    results = wikipedia.summary(query)
    speak("According to WikiPedia...")
    print(results)
    speak(results)

if __name__ =="__main__" :
    greeting()
   # wishMe()
    while True :
        query=TakeInput().lower()

        if 'wikipedia' in query:
            Wikipedia(query)

