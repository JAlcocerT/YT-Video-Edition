* https://platform.openai.com/docs/guides/speech-to-text

---

* https://jalcocert.github.io/JAlcocerT/useful-python-stuff/

```sh
python -m venv a2t_venv #create the venv
python3 -m venv a2t_venv #create the venv

#a2t_venv\Scripts\activate #activate venv (windows)
source a2t_venv/bin/activate #(linux)
```

Install them with:

```sh
#pip install openai
pip install -r requirements.txt #all at once
#pip freeze | grep openai

pip show openai
pip list
#pip freeze > requirements.txt #generate a txt with the ones you have!
```

```sh
source .env

#export OPENAI_API_KEY="your-api-key-here"
#set OPENAI_API_KEY=your-api-key-here
#$env:OPENAI_API_KEY="your-api-key-here"
echo $OPENAI_API_KEY
```