# based on https://github.com/mckaywrigley/takeoff-school-your-1st-ai-app

import os
import openai

# get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# loop until user types 'exit'
while True:
  question = input("What is your question? ")

  if question.lower() == "exit":
    print("Goodbye!")
    break
  
  # send the question to the API and receive the response
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant. Answer the given question."},
      {"role": "user", "content": question}
    ]
  )

  # print the response
  print(completion.choices[0].message.content + "\n")
