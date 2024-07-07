from openai import OpenAI
from keys import API_KEY
import os

client = OpenAI(api_key=API_KEY)   # defaults to getting the OPENAI_API_KEY from the environment

messages = [ {'role': 'system', 'content': 'You are an intelligent assistant.'} ]

while True:
    message = input('User: ')
    if message:
        messages.append(
            {'role': 'user', 'content': message},
        )
        chat = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)
    reply = chat.choices[0].message.content
    print(f'ChatGPT: {reply}')
    messages.append({'role': 'assistant', 'content': reply})

messages = [{'role': 'system', 'content': reply}] 

