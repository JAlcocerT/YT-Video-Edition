import openai

#export OPENAI_API_KEY='theapikey' # on Linux/Mac

#python3 text2audio-chatwithpdf.py


client = openai.OpenAI()
speech_file_path = "chatwithpdf-12-Closing.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input = "Let me know in the comments what are your plans to integrate this powerfull tool in your workflow. Stay tuned for more!"
)
response.stream_to_file(speech_file_path)


# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-11-test.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "And here we have the reply, look at that! You can now play with the prompts, feed more than one document or change the models to chat locally with your docs."
# )
# response.stream_to_file(speech_file_path)

# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-10-test.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "After few seconds, we have the PDF information already embedded on our FAISS DB, so we can now ask to the LLM about our secret paper."
# )
# response.stream_to_file(speech_file_path)



# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-9-dockerRun.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "And now, it seems that our container with the App is already running, so lets check the Streamlit UI in port 8501. Lets feed it again with a very secret paper, wait for the embedding model to process it and generate our vector DB."
# )
# response.stream_to_file(speech_file_path)


# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-8-dockerRun.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "These are just cosmetic changes that will allow us to feed the API keys via the Streamlit UI or directly as environment variable. \
#         And as mentioned, we will be using OpenAI as LLM model, FAISS as VectorDB and OpenAIEmbedding as Embedding Model. \
#             Now, lets just run our container image, let me do it with CLI this time, but you can also use Portainer like we did in previous videos."
# )
# response.stream_to_file(speech_file_path)

# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-7-Dockerbuild.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "Let's execute in paralel the docker build command, to create our Docker image of the streamlit app with langchain and embeddings."
# )
# response.stream_to_file(speech_file_path)


# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-6.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "The original App version require us to fill our OpenAI and HuggingFace API Keys in the dot env file. But as mentioned, I want to tweak it so that we will be asked direclty in the web UI to provide them."
# )
# response.stream_to_file(speech_file_path)


# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-5-Dockerfile.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "Let's create very quickly the Dockerfile to create the Docker container of the Streamlit App that Alejandro prepared. We can see which dependencies we need already here and we will expose port 8501."
# )
# response.stream_to_file(speech_file_path)


# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-4-theory.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "Last, but not least, we have our Large Language Model. We will be using GPT as our LLM, but you can also use some Open Source LLM like LLama2 or Mistral here. \
#         For the Vector DataBase, we will be using FAISS (Facebook AI Similarity Search), we could use other vector DBs like Pinecone or ChromaDB if we want an open source vector DB. \
#             The embedding model? we will go with OpenAI Embeddings, but we could also use Word2Vec or GloVe Open Source models."
# )
# response.stream_to_file(speech_file_path)


# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-3-theory.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "It is one hour long of valuble content, but if you are in a rush, let me tell you the key concepts you need to know. \
#         A LangChain is a framework designed to facilitate the creation and integration of conversational AI applications by using language models and various NLP tools. \
#          LangChain uses embeddings to help computers understand language. It takes words and sentences, turns them into these special number codes (embeddings), and then uses them to make the computer do things like chat or answer questions. \
#          The vector databases come into play by storing all these number codes. When LangChain needs to understand something written or figure out how to respond to a question, it looks up the right codes in the vector database.      \
#             Think of a vector database as a huge library where all these number codes (embeddings) are stored. Every word or sentence that's turned into a code gets its own spot in this library."
# )
# response.stream_to_file(speech_file_path)

# client = openai.OpenAI()
# speech_file_path = "chatwithpdf-1-intro.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input = "Today, I want to show you how to tweak the fantastic work Alejandro made on his very popular video about LangChain App with Python. \
#         Following previous videos structure, I will show you how to create the Docker container for the Streamlit App and will present you with \
#             a more user friendly version of it, that allow us to input the API keys directly on the UI interface."
# )
# response.stream_to_file(speech_file_path)


# Setting Up the Environment: The tutorial begins with setting up a virtual environment and installing necessary dependencies like Python 3.9, Streamlit for the GUI, PyPDF2 for reading PDFs, LangChain for interacting with language models, and other packages for handling files and secrets.

# Building the Graphical User Interface (GUI): The instructor demonstrates creating a GUI using Streamlit, including setting page configurations, adding headers, creating a text input for questions, and a sidebar for uploading PDF documents.


# Embedding models and large language models (LLMs) are both powerful tools in the field of natural language processing (NLP). However, they serve different purposes and have distinct characteristics.

# Embedding models are designed to convert discrete units of text, such as words or phrases, into dense vectors of numbers. These vectors capture the semantic and syntactic relationships between the words, allowing them to be used for a variety of tasks, including machine translation, sentiment analysis, and text similarity.

# LLMs, on the other hand, are more complex models that can generate human-quality text, translate languages, write different kinds of creative content, and answer your questions in an informative way. They are trained on massive amounts of text data and are able to learn the patterns and relationships between words and phrases.

# The main idea with embeddings, is that The large string of text is then divided into smaller chunks. These chunks are converted into embeddings (vector representations of text) using either OpenAI's models (paid service) or Hugging Face's Instructor embeddings (free but requires more computational resources).

# Then, the embeddings are stored in a vector store, basically a database, which is used for semantic search to find text chunks relevant to user queries.

# When a user asks a question, the application searches the vector store for relevant text chunks and sends them as context to a language model. The language model then generates an answer based on this context.


# LangChain uses embeddings to help computers understand language. It takes words and sentences, turns them into these special number codes (embeddings), and then uses them to make the computer do things like chat or answer questions.

# The vector databases come into play by storing all these number codes. When LangChain needs to understand something written or figure out how to respond to a question, it looks up the right codes in the vector database.

# Think of a vector database as a huge library where all these number codes (embeddings) are stored. Every word or sentence that's turned into a code gets its own spot in this library. 