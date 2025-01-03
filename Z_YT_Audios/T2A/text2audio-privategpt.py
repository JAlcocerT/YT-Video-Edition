import openai

#export OPENAI_API_KEY='theapikey' # on Linux/Mac

#python3 text2audio-privategpt.py



client = openai.OpenAI()
speech_file_path = "PrivateGPT-7-end.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input = "I just test it with a veeeery secret paper about a P2P electronic cash project. And here is how PrivateGPT does it magic. \
        Let me know in the comments what plans you have to use PrivateGPT for. Don't forget to stay tuned for more exciting content!"
)
response.stream_to_file(speech_file_path)


# client = openai.OpenAI()
# speech_file_path = "PrivateGPT-4-DeployPrivateGPT.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "After a while, we have PrivateGPT Docker container ready to be deployed. \
#     We can now just use docker-compose up command to deploy it, or use Portainer as I did here."
# )
# response.stream_to_file(speech_file_path)

# client = openai.OpenAI()
# speech_file_path = "PrivateGPT-3-Dockerfile.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "Next up, we're going to craft a Dockerfile that mirrors the installation steps outlined on the PrivateGPT documentation page. \
#          This one time step is key for setting up a standalone Python container loaded with all the necessary PrivateGPT dependencies. \
#              The beauty of this? Once done, you can use PrivateGPT on any computer or deploy to the cloud if you want to."
# )
# response.stream_to_file(speech_file_path)


# client = openai.OpenAI()
# speech_file_path = "PrivateGPT-2-GH.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input=" I will show you a quick and easy setup of PrivateGPT on your local machine. With just THREE simple commands, \
#         thanks to Docker, you can get PrivateGPT up and running in no time! And the best part? \
#              You don't need any developer skills or Python installation. "
# )
# response.stream_to_file(speech_file_path)


# PrivateGPT documentation is great and they guide properly Python users to install all dependencies and get the project running. 

# client = openai.OpenAI()
# speech_file_path = "PrivateGPT-1-GH.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input="In today's video, we're diving into PrivateGPT, an open-source project that's changing the game. \
#     Imagine chatting with your documents right on your local machine, with no GPU needed!"
# )
# response.stream_to_file(speech_file_path)


# 
# client = openai.OpenAI()
# speech_file_path = "PrivateGPT-1-GH.mp3"
# response = client.audio.speech.create(
    # model="tts-1",
    # voice="onyx",
    # input="Let me know in the comments which of the newest LLM's you want me to try with this super easy way. Let's enjoy and create awsome software!"
# )
# response.stream_to_file(speech_file_path)