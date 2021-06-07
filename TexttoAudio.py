from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
language="en"
file_tobe_read=open(r"F:\\Projects\\read.txt","r").read()
speech=gTTS(text=str(file_tobe_read),lang=language,slow=False)
speech.save(audio)
if playsound(audio)!=False:
    print("Did you hear it................???")
else:
    print("Check the configurations and install the modules correctly....!!!")    