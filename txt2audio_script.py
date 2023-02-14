from gtts import gTTS
import os

# specify the file path and name
file_path = ".\texto.txt"

# open the file in read mode
with open(file_path, "r", encoding="utf-8") as file:
    # read the contents of the file
    file_contents = file.read()
    # convert the text to speech
    tts = gTTS(file_contents, lang='pt-br')
    # save the speech to a file
    tts.save("AudioConvertido.mp3")
    # play the speech
    os.system("AudioConvertido.mp3")
