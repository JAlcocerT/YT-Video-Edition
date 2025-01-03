import openai

#https://platform.openai.com/api-keys
#export OPENAI_API_KEY='sk-...' # on Linux/Mac

#cd ai-openai
#python3 texttoaudio.py

##################### NETDATA OLLAMA YT ###################################

#After you will watch this video, you will know how to Monitor your server while performing AI workloads, all locally, this time thanks to the NetData.
#Before moving on, remember that you will need Docker installed on your machine, together with Portainer to follow along. I will leave the commands below if you need to Setup those.
#Also, make sure you have some Local AI project to test NetData out. For example you can follow along the Ollama installation and pull some Free Model, like Orca-mini.
#Now, lets just login to Portainer and create a new Stack. And yes, you will find this information in the video description. 
#And today, we just need one artifact, the docker-compose, that will configure and spin up our Netdata instance thanks to the already existing Docker container. So yea, today no python scripts, no docker builds
#Lets just create our stack with Portainer and lets wait for the service to be deployed. The idea is that we will have historical monitoring data for our laptops when we are running LLMs locally. But same process applies if you want to run them on big servers and monitor them.
#And now, the fun part. Lets use Ollama, which we already covered how to install locally here. Lets make it use Mistral and ask something to the model. You can see how the increase of temperature is being registered
#Let me know in the comments which workloads you cant wait to monitor with Netdata. Consider giving a like to the video if it was helpful!And stay tuned for more.

# timeline
#     title Monitoring AI Infrastructure with NetData
#     Pre-Requisites : Get Docker 🐋
#                    : Install Portainer
#                    : Have Ollama Ready with a local LLM
#     SelfHosting Netdata : Using the Docker-Compose Stack
#     NetData + Ollama : Overview to Netdata
#                      : Running prompts with Ollama
#                      : Checking System Load and Temps 🔥

client = openai.OpenAI()
speech_file_path = "Netdata10.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input="Let me know in the comments which workloads you cant wait to monitor with Netdata. Consider giving a like to the video if it was helpful!And stay tuned for more."
)
response.stream_to_file(speech_file_path)




##################### OLLAMA YT ###################################

#In this video, I am going to show you how to use LLMs locally, this time thanks to the Ollama Project.
#Before we start, make sure you have installed Docker and have Portainer running, as I will show you how to deploy Ollama through its UI and then we will try the Orca LLM. I will give you some extra tips to get the most out of Ollama as well.
#In the Ollama's website, we can browse the Free LLMs that are compatible at this moment with the project, we can choose any of these models, which come in different sizes, to fit from our consumer hardware to powerful cloud servers if we want
#Ollama is an Open Source Project and just in the main page we can see that we can make a direct installation, but the project also comes with its own created container (which we will use right now), so no Dockerfiles this time.
#Let me show you the Docker Compose Stack, the only thing that we will need today to deploy Ollama. You can see that we are referencing the docker image at dockerhub, with the latest version and that we are using the default, 11434 port to interact with the Ollama and the models."
#Lets go to Portainer, Stacks and create a new one with our configuration. As of now, the latest Docker image version it is zero point one point 17, you can choose a specific version if you want. "

#Now, we can go inside the deployed container and check Ollama's version, which is 0.1.9 and...list the available containers, for now it is empty, but lets give it a spin with the orca LLM.

#The Ollama run command, will download first and then make available any LLM that it is listed in the project side. You can run falcon, code wizzard, llama and the compatible model list grows over time.
#Now, this is one way to interact with the models through the Docker container terminal. Let's make the orca model some question

#And this is it, here we have the orca model replying to us. Let me show you in real time the task manager so you can get a feel of the speed on my laptop. The answers sounds pretty legit, right?

#While it completes, let me explain you other way to interact with Ollama, as we can also do it through a curl command which make it accesible through http requests"
#Just make sure that Ollama is running, and then call the REST API with the http request, like this one here, which will give you only the response part of the full output json

#In this case, I have selected not to stream, so we will get just the final reply from the Orca, explaining what it is Docker as an example.
#And yes,I said a second way, because there are more possibilities to use Ollama. As you can see, there are other projects that are being built on top of it. From chat UI's, Vector Database with MindsDB, even possibility to be plugged into Logseq, which if you didnt know, it is a privacy first knowledge base.
#Let me quickly show you a third option to use Ollama. THis time with Python, thanks to LLama-Index, we just need literally 3 lines of code to interact with LLMs
#Just remember to have Ollama running with your desired LLM, pip install llama-index and you are ready to go.
# Let me know in the comments which particular integration of Ollama with LogSec, Home Assistant or any other you want to see for the next videos. Projects like Ollama are worth exploring, as they are trully making Generative AI accessible to everyone.
#And while Orca LLM tells us what it is A vector database, consider giving a like to the video if it was helpful! And share, dont forget to share with others what you've learnt.

# client = openai.OpenAI()
# speech_file_path = "Testing10.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input="And while Orca LLM tells us what it is A vector database, consider giving a like to the video if it was helpful! And share, dont forget to share with others what you've learnt."
# )
# response.stream_to_file(speech_file_path)


#######################################################




# client = openai.OpenAI()
# speech_file_path = "5final.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input="Let me know in the comments which of the newest LLM's you want me to try with this super easy way. Let's enjoy and create awsome software!"
# )
# response.stream_to_file(speech_file_path)




################################3


# import openai

# #export OPENAI_API_KEY='theapikey' # on Linux/Mac

# client = openai.OpenAI()
# speech_file_path = "4end.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input="Just copy it from the gist in the video description and deploy a new Stack. That's it, text gen web ui is waiting for us in port 7860 to download and use any LLM."
# )
# response.stream_to_file(speech_file_path)

# import openai

# #export OPENAI_API_KEY='theapikey' # on Linux/Mac

# client = openai.OpenAI()
# speech_file_path = "3docker.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input="Now, lets build our Docker image and use this stack that I prepared to deploy it with Portainer."
# )
# response.stream_to_file(speech_file_path)



# import openai

# #export OPENAI_API_KEY='theapikey' # on Linux/Mac

# client = openai.OpenAI()
# speech_file_path = "3docker.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input="We will clone the original project's repository and use Docker to install the dependencies reliably. I have adjusted the Dockerfile so that it runs for CPUs and everyone can use it, but feel free to adapt it if you have a  powerfull GPU."
# )
# response.stream_to_file(speech_file_path)


# import openai


# #export OPENAI_API_KEY='theapikey' # on Linux/Mac

# client = openai.OpenAI()
# speech_file_path = "intro.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input="We are going to see how to use The Text Generation Web UI, to run any Large Language Model locally for free!"
# )
# response.stream_to_file(speech_file_path)
