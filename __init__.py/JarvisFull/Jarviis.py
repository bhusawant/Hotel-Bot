

from Body.Listen import Listen
from Body.Speak import Speak


def MainExe():
    
    Speak("Main Execution Has Been Started")
    
    while True:
        
        query = Listen()
        
        if "hello" in query:
            Speak("Hi! I am Jarvis!")
        
        elif "bye" in query:
            Speak("Hello Bye.")
        
        elif "sonu" in query:
            Speak("Sonu is the boy")
        
        elif "aditi" in query:
            Speak("Aditi is a girl")
MainExe()
        