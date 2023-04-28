import os
import openai

# get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# send the question to the API and receive the response
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Say Hello World in the style of a pirate."
    }
  ]
)

# print the response
print("\n"+completion.choices[0].message.content)
