import speech_recognition #語音辨識
import pyaudio
from gtts import gTTS     #語音合成
from pygame import mixer
import tempfile 
mixer.init()
r = speech_recognition.Recognizer()
print("開始辨識")
speech_text = ""
try:
    with speech_recognition.Microphone() as source:
        audio=r.listen(source)
    speech_text=(r.recognize_google(audio,language='zh-TW'))
    print(speech_text)
    
except :
    print("沒有資料")


def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence,lang='zh')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load("{}.mp3".format(fp.name))
        mixer.music.play()
        
speak(speech_text)

