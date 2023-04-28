import os
import PyPDF2
import openai

# get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# initialize summary
pdf_summary_text = ""

# read the pdf
pdf_file = open("doc/whitepaper.pdf", 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# loop over pages
for page_num in range(len(pdf_reader.pages)):
  page_text = pdf_reader.pages[page_num].extract_text().lower()

  # request the summary of one page
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[ 
      {"role": "user", "content": f"Summarize this: {page_text}"},
    ],
  )

  # append the page summary
  pdf_summary_text += response["choices"][0]["message"]["content"] + "\n\n"

  # write the results to file
  with open("doc/whitepaper_summary.txt", "w+") as file:
    file.write(pdf_summary_text)

pdf_file.close()
