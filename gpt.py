import requests
import openai
import os
from dotenv import load_dotenv

import os
import openai
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt_response(prompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
    ], 
    max_tokens=100
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

if __name__ == '__main__':
    gpt_response("welcome me")