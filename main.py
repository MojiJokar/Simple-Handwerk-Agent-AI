import os
from dotenv import load_dotenv

from agent import CustomerAgent
from crm import CRM
from email_service import get_new_email


load_dotenv()

#API_KEY = os.getenv("OPENAI_API_KEY")
API_KEY = os.getenv("NVIDIA_API_KEY")


def main():

    print("AI Agent started...")

    # -----------------------
    # 1. دریافت ایمیل
    # -----------------------

    email = get_new_email()

    print("\nIncoming email:")
    print(email)


    # -----------------------
    # 2. ساخت Agent
    # -----------------------

    agent = CustomerAgent(API_KEY)


    # -----------------------
    # 3. تحلیل ایمیل
    # -----------------------

    result = agent.analyze_email(email)

    print("\nAI result:")
    print(result)


    # -----------------------
    # 4. اتصال به CRM
    # -----------------------

    crm = CRM()


    customer = result["customer"]

    existing_customer = crm.find_customer(
        customer["email"]
    )


    # -----------------------
    # 5. تصمیم
    # -----------------------

    if existing_customer:

        print("\nExisting customer found.")

    else:

        print("\nNew customer.")

        crm.create_customer(customer)


    # -----------------------
    # 6. پاسخ
    # -----------------------

    print("\nSuggested response:")

    print(result["response_text"])


if __name__ == "__main__":
    main()