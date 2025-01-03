# import whisper

# # Load the Whisper model
# model = whisper.load_model("base") 

# # Path to your audio file
# audio_file = "/home/jalcocert/Videos/audio.mp3" 

# # Transcribe the audio
# result = model.transcribe(audio_file)

# # Save the transcription to a file
# with open("transcription.txt", "w") as f:
#     f.write(result["text"])

# print("Transcription saved to transcription.txt")

# # import openai

# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # # Get the OpenAI API key from the environment variables
# # api_key = os.getenv("OPENAI_API_KEY")


# # # Replace with your actual OpenAI API key
# # #openai.api_key = "YOUR_OPENAI_API_KEY"

# # def transcribe_audio(audio_file_path):
# #   """
# #   Transcribes an audio file using OpenAI's Whisper API.

# #   Args:
# #     audio_file_path: Path to the audio file (.mp3).

# #   Returns:
# #     The transcribed text.
# #   """

# #   with open(audio_file_path, "rb") as audio_file:
# #     transcription = openai.Audio.transcriptions.create(
# #         model="whisper-1", 
# #         file=audio_file
# #     )

# #   return transcription.text

# # # Example usage:
# # audio_file = "/home/jalcocert/Videos/audio.mp3" 
# # transcribed_text = transcribe_audio(audio_file)

# # print(transcribed_text)

