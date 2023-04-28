import os
import openai

# get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# generate an image
response = openai.Image.create(
  prompt="award-winning picture of T-rex playing a ukulele",
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']
print(image_url)
