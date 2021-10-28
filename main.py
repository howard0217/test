import speech_recognition #語音辨識
#import pyaudio
from gtts import gTTS     #語音合成
from pygame import mixer
import tempfile 
from flask import Flask
from flask.templating import render_template
import Chatbot.chatbot as cb

chatter = cb.Chatbot(w2v_model_path='word2vec.model')

mixer.init()
r = speech_recognition.Recognizer()

def speech_recognize():
    print("開始辨識")
    try:
        with speech_recognition.Microphone() as source:
            audio=r.listen(source, 10, 3)

        speech_text=(r.recognize_google(audio,language='zh-TW'))
        print(speech_text)
        return speech_text
        
    except :
        a="沒有資料"
        return a


def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence,lang='zh')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load("{}.mp3".format(fp.name))
        mixer.music.play()
        

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/start/', methods = ["POST", "GET"])
def recognize_and_start():
    print('entered')
    text = speech_recognize()
    res = chatter.get_response(text)
    speak(res)

    return render_template('main.html', recognized_text = res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=False)
