import openai

# Set up your API key
openai.api_key = '<your open ai key>'

# Define your prompt
prompt = input("Enter your prompt: ")

# Generate text using the prompt with GPT-3.5 engine
response = openai.Completion.create(
  engine="gpt-3.5-turbo-instruct",  # GPT-3.5 engine
  prompt=prompt,
  max_tokens=2000  # Adjust as needed
)

# Print the generated text
print(response.choices[0].text.strip())

