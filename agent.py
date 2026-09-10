import json
from openai import OpenAI

from models import CustomerRequest, AgentDecision
from prompts import SYSTEM_PROMPT


class CustomerAgent:

    def __init__(self, api_key: str):

        self.client = OpenAI(
            api_key=api_key
        )

    def analyze_email(self, email_text: str):

        response = self.client.chat.completions.create(

            model="gpt-4o-mini",

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": email_text
                }
            ],

            response_format={
                "type": "json_object"
            }
        )

        result = response.choices[0].message.content

        return json.loads(result)