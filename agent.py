from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class CustomerAgent:

    def __init__(self):
        api_key = os.getenv("NVIDIA_API_KEY")
        base_url = os.getenv("NVIDIA_BASE_URL")

        # Test: API values
        print(f"NVIDIA_API_KEY: {api_key}")
        print(f"NVIDIA_BASE_URL: {base_url}")

        if not api_key:
            raise ValueError("NVIDIA_API_KEY is missing from .env")

        if not base_url:
            raise ValueError("NVIDIA_BASE_URL is missing from .env")

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=120  # Set a timeout of 120 seconds
        )

    # !!! AFTER TESTING NVIDIA, DUE TO likely the larger prompt/request
    # configuration, WE MAKE A SIMPLER VERSION

    def analyze_email(self, email):
        print("Sending request to NVIDIA...")

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Extract information from this customer email.

Email:

{email}

Return ONLY valid JSON,
Do not explain anything.
Do not show  your reasoning.
Use exactly this structure:

{{
    "customer_name": "",
    "location": "",
    "problem": "",
    "requested_appointment": "",
    "urgency": "",
    "category": ""
}}
"""
                }
            ],
            temperature=0,
            max_tokens=1000,
            extra_body={
                "chat_template_kwargs": {
                    "enable_thinking": False
                }
            }
        )

        # print("Response received from NVIDIA!")

        # message = response.choices[0].message

        # print("\nMESSAGE OBJECT:")
        # print(message)

        # print("\nCONTENT:")
        # print(repr(message.content))

        # print("\nREASONING:")
        # print(repr(message.reasoning))

        # print("\nREASONING CONTENT:")
        # print(repr(message.reasoning_content))

        # return message.content
        
        print("FINISH REASON:")
        print(response.choices[0].finish_reason)
        
        
        result = response.choices[0].message.content

        print("AI RESULT:")
        print(result)

        return result
