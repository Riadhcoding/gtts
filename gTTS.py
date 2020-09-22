# Google Text To Speech
# this script run in python3
# pip install gTTS
# www.youtube.com/c/pythonlife

from gtts import gTTS
import os
i = input("Entre you Name : ")
tx = ("hey" +i+ " welcome to my tool please dont forget to subscribe to my channel to learn more")

ln = 'en'

out = gTTS(text=tx , lang=ln , slow=False )

out.save('voice1.mp3')

os.system('start voice1.mp3')

