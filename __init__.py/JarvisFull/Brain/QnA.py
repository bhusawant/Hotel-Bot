# Api Key

fileopen = open("Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()


# Importing
import openai
from dotenv import load_dotenv
from Body.Listen import Listen, TranslationHinToEng
from Body.Speak import Speak
#Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QuestionAnswer(question,chat_log = None):
    FileLog = open("Database\\QnA_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()
    
    if chat_log is None:
        chat_log = chat_log_template
    
    prompt = f'{chat_log}Question : {question}\nAnswer : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    FileLog = open("Database\\QnA_log.txt",'w')
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer



while True:
    k = Listen()
    kk = str(TranslationHinToEng(k))
    a = str(QuestionAnswer(kk))
    Speak(a)