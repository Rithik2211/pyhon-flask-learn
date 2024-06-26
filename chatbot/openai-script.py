from openai import OpenAI

def llm(question, content):
  # Point to the local server
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

  passlllm = f'Question:{question}\n Content:{content}'
  print(passlllm)
 # prompt template
  completion = client.chat.completions.create(
    model="TheBloke/Llama-2-7B-Chat-GGUF",
    messages=[
      {"role": "system", "content": "You are a Q&A Chatbot intracting with real-world customers to their questions. Only answer based on the content provided. Do not provide any information that is not in the content. Answer in a intercative way"},
      {"role": "user", "content": passlllm}
    ],
    temperature=0.7,
  )

  return completion.choices[0].message.content

print(llm("What is India?", "India is a country world."))
