#python3 pyopen.py > output.mdx

import os
from dotenv import load_dotenv
from openai import OpenAI  # pip install openai>0.28

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
)

system_must_have= """
This is a system message.
You will help to create interesting video title and video description for the given audio transcriptions.
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": f"""You are an expert in SEO and youtube. Very aware of the following:
                              {system_must_have}  
                        """,
        },
        {"role": "user", "content": f"""Please create a video title and video description for this {}"""}

    ],
    model="gpt-4o-mini",
    temperature=0.8,
)

# print(chat_completion)
# Extract and print the content of the completed message
completed_message = chat_completion.choices[0].message.content
print(completed_message)