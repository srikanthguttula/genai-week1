import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Start conversation with a system message
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print(" Chatbot is running. Type 'exit' to quit.\n")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting chat.")
            break

        # Append user input to message history
        messages.append({"role": "user", "content": user_input})

        # Call OpenAI Chat API
        response = client.chat.completions.create(
            model="gpt-4o",  # Or "gpt-3.5-turbo"
            messages=messages
        )

        reply = response.choices[0].message.content
        print(f"Bot: {reply}")

        # Append assistant response to messages
        messages.append({"role": "assistant", "content": reply})

        # Log to file
        with open("log.txt", "a") as log_file:
            log_file.write(f"You: {user_input}\nBot: {reply}\n\n")

    except Exception as e:
        print("⚠️ An error occurred:", str(e))
