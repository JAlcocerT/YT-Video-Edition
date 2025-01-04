from openai import OpenAI
#https://platform.openai.com/docs/guides/speech-to-text

import os
from dotenv import load_dotenv

load_dotenv()

# # # Get the OpenAI API key from the environment variables
# # api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

####ffmpeg -i capture0001.wav output.mp3
###python3 ./A2T/openais2t.py

audio_file= open("/home/jalcocert/Videos/output.mp3", "rb")
#audio_file= open("/home/jalcocert/Videos/capture0000.wav", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)

text_to_write = transcription.text

# Open the text file in write mode ('w') and write the content
with open("transcription0004.txt", "w") as text_file:
  text_file.write(text_to_write)

print("Transcription written to transcription.txt")