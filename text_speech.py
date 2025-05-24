pip install gtts
from gtts import gTTS
import os

text = "Hey there we are doing a small project"
language = 'en'

speech = gTTS(text = text, lang =  language , slow = false)

speech.save("output.mp3")
os.system("open output.mp3")
