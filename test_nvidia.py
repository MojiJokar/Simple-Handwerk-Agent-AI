from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")
base_url = os.getenv("NVIDIA_BASE_URL")

print("API key loaded:", bool(api_key))
print("Base URL:", base_url)

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
    timeout=30.0
)

print("Client created.")
print("Sending request...")

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Say HELLO"
        }
    ],
    max_tokens=50,
    temperature=0,
    extra_body={
        "chat_template_kwargs": {
            "enable_thinking": False
        }
    }
)

print("Response received!")
print(response)