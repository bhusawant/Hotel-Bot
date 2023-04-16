# Hindi or English - Command
# English

# Step - 1
# pip install googltrans==3.1.0a0

# Step - 2
# Three Functions
# 1 - Listen function
# 2 - English Translation
# 3 - Connect

import speech_recognition as sr
from googletrans import Translator

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
    return query

# print(Listen())

# 2 - Translator

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line,language='en')
    data = result.text
    print(f"You : {data}.")
    return data
# TranslationHinToEng("और भाई क्या हाल है सत्यमेव जयते")

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

