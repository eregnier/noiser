
from gtts import gTTS
import os
from flask import Flask, request, send_file
import platform
app = Flask(__name__)
import logging

logging.basicConfig(filename='history.log', filemode='w', level=logging.INFO, format='%(asctime)s %(message)s')



@app.route('/speak', methods=["POST"])
def speak():
    text = request.form.get('text')
    prefix = request.form.get('prefix', 'message')
    lang = request.form.get('lang', 'en')
    print(request.form)
    logging.info(text)
    tts = gTTS(text=f"{prefix} : {text}", lang=lang)
    tts.save("text.mp3")
    if platform.system() == 'Windows':
        vlc_command = '"C:/Program Files/VideoLAN\VLC/vlc.exe"'
    else:
        vlc_command = 'vlc'
    out = os.popen(f"{vlc_command} -I dummy text.mp3 vlc://quit").read()
    print(out)
    return text

@app.route('/')
def index():
    return send_file('index.html')