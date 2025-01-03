from openai import OpenAI

#export OPENAI_API_KEY='theapikey' # on Linux/Mac


client = OpenAI()


# client = OpenAI(
#     api_key="My API Key",  # Replace with your actual API key
# )


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What do you know about Flutter?",
        }
    ],
    model="gpt-3.5-turbo",  # Replace with the correct model name: 
)


# Assuming 'chat_completion' is the response object from the client.chat.completions.create call
for choice in chat_completion.choices:
    message = choice.message
    if message.role == "assistant":
        print(message.content)  # This will print the content of the message from the assistant



# # Assuming 'chat_completion' is the response object from the client.chat.completions.create call
# token_usage = chat_completion.usage

# # Total tokens used in the completion
# total_tokens = token_usage.total_tokens

# # Approximate cost calculation (if you know the cost per token)
# cost_per_token = 0.06 / 1000  # Replace X with the actual cost per token # https://openai.com/pricing
# approx_cost = total_tokens * cost_per_token

# print(f"Total tokens used: {total_tokens}")
# print(f"Approximate cost: {approx_cost}")