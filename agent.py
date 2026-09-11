# import json
# from openai import OpenAI

# from models import CustomerRequest, AgentDecision
# from prompts import SYSTEM_PROMPT


# class CustomerAgent:

#     def __init__(self, api_key: str):

#         self.client = OpenAI(
#             api_key=api_key
#         )

#     def analyze_email(self, email_text: str):

#         response = self.client.chat.completions.create(

#             model="gpt-4o-mini",

#             messages=[
#                 {
#                     "role": "system",
#                     "content": SYSTEM_PROMPT
#                 },
#                 {
#                     "role": "user",
#                     "content": email_text
#                 }
#             ],

#             response_format={
#                 "type": "json_object"
#             }
#         )

#         result = response.choices[0].message.content

#         return json.loads(result)
############UPDATED CODE############
# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# class CustomerAgent:

#     def __init__(self):
#         self.client = OpenAI(
#             api_key=os.getenv("NVIDIA_API_KEY"),
#             base_url="https://integrate.api.nvidia.com/v1"
#         )

#     def analyze_email(self, email):

#         response = self.client.chat.completions.create(
#             model="meta/llama-3.1-8b-instruct",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": """
# You are an AI agent for a German Handwerk company.

# Analyze incoming customer emails and extract:
# - customer name
# - location
# - problem
# - requested appointment
# - urgency
# - category

# Return the information clearly.
# """
#                 },
#                 {
#                     "role": "user",
#                     "content": email
#                 }
#             ],
#             temperature=0.2,
#             max_tokens=500
#         )

#         return response.choices[0].message.content
##########simplest version =================================
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class CustomerAgent:

    def __init__(self):
        api_key = os.getenv("NVIDIA_API_KEY")
        base_url = os.getenv("NVIDIA_BASE_URL")
        # Test: api are tested :
        print(f"NVIDIA_API_KEY: {api_key}")
        print(f"NVIDIA_BASE_URL: {base_url}")
        if not api_key:
            raise ValueError("NVIDIA_API_KEY is missing from .env")

        if not base_url:
            raise ValueError("NVIDIA_BASE_URL is missing from .env")

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def analyze_email(self, email):

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an AI agent for a German Handwerk company.

Analyze incoming customer emails and extract:

- customer name
- location
- problem
- requested appointment
- urgency
- category

Return the information clearly.
"""
                },
                {
                    "role": "user",
                    "content": email
                }
            ],
            temperature=0.2,
            max_tokens=500
        )

        return response.choices[0].message.content