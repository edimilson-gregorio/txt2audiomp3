from gtts import gTTS
import os

# specify the file path and name
file_path = "txt file path"

# open the file in read mode
with open(file_path, "r", encoding="utf-8") as file:
    # read the contents of the file
    file_contents = file.read()
    # convert the text to speech
    tts = gTTS(file_contents, lang='pt-br')
    # save the speech to a file
    tts.save("mp3 file name")
    # play the speech
    os.system("mpg321 mp3 file name")
