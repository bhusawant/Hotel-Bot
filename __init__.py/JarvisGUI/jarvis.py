import sys
from tkinter import *
from PIL import ImageTk, Image
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType


from jarvisUI import Ui_JARVIS
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia





from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
...


chrome_options = Options()
chrome_options.add_argument('--log-level=3')  # avoid unecessary msgs from selenium
chrome_options.headless = True  # chrome will open in background,we can't see that
Path = "JarvisGUI/Database/chromedriver.exe"
driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon sir")
    else:
        Speak("Good Evening Sir")
    Speak("How may i help you?")



def Speak(Text):
    lengthoftext = len(str(Text))
    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f"AI:{Text}")
        Data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'  # to avoid error
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()

        if lengthoftext >= 30:
            sleep(4)
        elif lengthoftext >= 40:
            sleep(6)
        elif lengthoftext >= 55:
            sleep(8)
        elif lengthoftext >= 70:
            sleep(10)
        elif lengthoftext >= 100:
            sleep(13)
        elif lengthoftext >= 120:
            sleep(14)
        else:
            sleep(2)




class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()


    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("")
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print("User Said : ", self.query)

        except Exception as e:
            print("")
            return "None"
        return self.query

    def TaskExecution(self):
        wish()
        while True:
            # Api Key

            fileopen = open(r"JarvisGUI\Data\Api.txt","r")
            API = fileopen.read()
            fileopen.close()
            print(API)

            # Importing
            import openai
            from dotenv import load_dotenv

            #Coding

            openai.api_key = API
            load_dotenv()
            completion = openai.Completion()

            def ReplyBrain(question,chat_log = None):
                FileLog = open(r"JarvisGUI\DataBase\chat_log.txt","r")
                chat_log_template = FileLog.read()
                FileLog.close()
                
                if chat_log is None:
                    chat_log = chat_log_template
                
                prompt = f'{chat_log}You : {question}\nJarvis : '
                response = completion.create(
                    model = "text-davinci-002",
                    prompt=prompt,
                    temperature = 0.5,
                    max_tokens = 30,
                    top_p = 0.3,
                    frequency_penalty = 0.5,
                    presence_penalty = 0
                )
                answer = response.choices[0].text.strip()
                chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
                FileLog = open(r"JarvisGUI\DataBase\chat_log.txt",'w')
                FileLog.write(chat_log_template_update)
                FileLog.close()
                return answer

            while True:
                
                kk = self.takeCommand()
                if "facilities" in kk:
                    Speak("Here are some facilities")
                    os.system(f'python {"JarvisGUI/GUI/Facilities/Facilities.py"}')
                elif "nearby" in kk:
                    Speak("Here are some nearby places")
                    os.system(f'python {"JarvisGUI/GUI/Nearby/nearby.py"}')
                if "terminate" in kk:
                    Speak("Bye Sir , Have a nice day!")
                    # self.ui.pushButton_2.clicked.connect(self.close)
                    self.ui.pushButton_2.clicked.connect(self.feedback)
                Speak(ReplyBrain(kk))
    
            

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JARVIS()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        # self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.feedback)


    def startTask(self):
        self.ui.movie = QtGui.QMovie("JarvisGUI/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("JarvisGUI/Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def feedback(self):
        os.system(f'python {"Feedback.py"}')
        os.close(f'python {"JarvisGUI/jarvis.py"}')

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
