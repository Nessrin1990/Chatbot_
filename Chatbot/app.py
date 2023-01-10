# -*- coding: utf-8 -*-
"""


@author: nesrine azaiez 
"""
from gtts import gTTS
import os
import time
from flask import Flask, render_template, request
import chatbot
from datetime import datetime

app = Flask(__name__)
#app.static_folder = 'static'

@app.route("/")
def home():

    ## In your route...

    #now = datetime.now()  # current date and time
    #date_time = now.strftime(" %H:%M")

    #return render_template('index.html', date_time=date_time
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    output1 = gTTS(text=userText, lang='en', slow=True)
    output1.save("output1.wav")
    os.system("start output1.wav")
    time.sleep(1)
    response = chatbot.chatbot_response(userText)
    output= gTTS(text=response, lang='en', slow=True)
    output.save("output.wav")
    os.system("start output.wav")
    time.sleep(1)
    return str(chatbot.chatbot_response(userText))



if __name__ == '__main__':
    app.run(threaded = False)
