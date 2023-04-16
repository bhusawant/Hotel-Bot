# Running 


import os
import speech_recognition as sr

# 1 - Listen : Hindi or English

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # listen(x,y,z) where z is the time after which jarvis reply
        # if there is no voice
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = "en")
        
    except:
        return ""

    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    queery = Listen().lower()
    
    if "wake up" in queery:
        os.startfile(r"Y:\Jarvis\main.py")
        
    else:
        pass
