
* [Setup Python](https://jalcocert.github.io/JAlcocerT/guide-python/#installing-python-) and [install the requirements](https://jalcocert.github.io/JAlcocerT/useful-python-stuff/):


* See <https://jalcocert.github.io/JAlcocerT/my-youtube-ai-workflow/#quick-vlogs-as-a-code>

```sh
python3 --version #3.10.12
python --version #3.7.9 (installed with chocolatey)
#Set-ExecutionPolicy RemoteSigned


pip install moviepy #==1.0.3 #https://github.com/Zulko/moviepy
pip install pymediainfo #==6.1.0
```


```sh
pip install pillow #for watermarks
```

---

## Venv Setup

```sh
#git clone https://github.com/JAlcocerT/openai-chatbot

#python --version
python3 -m venv video_python_venv #create a Python virtual environment
#python -m venv video_python_venv

video_python_venv\Scripts\activate #activate venv (windows)
#source video_python_venv/bin/activate #(linux)

#deactivate #when you are done


pip install -r requirements.txt


source .env
#export GROQ_API_KEY="your-api-key-here"
#set GROQ_API_KEY=your-api-key-here
#$env:GROQ_API_KEY="your-api-key-here"
echo $GROQ_API_KEY $OPENAI_API_KEY $ANTHROPIC_API_KEY

streamlit run Z_ST_AIssistant_v1.py

# git add .
# git commit -m "better st offer analyzer"
# git push
```