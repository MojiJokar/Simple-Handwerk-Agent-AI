import os
from dotenv import load_dotenv

from agent import CustomerAgent
from crm import CRM
from email_service import get_new_email


load_dotenv()

#API_KEY = os.getenv("OPENAI_API_KEY")
#API_KEY = os.getenv("NVIDIA_API_KEY")


def main():

    print("\nAI Agent started...")

    # -----------------------
    # 1. receive email
    # -----------------------

    email = get_new_email()

    print("Incoming email:")
    print(email)
    print("----test--email is printed-----------------")


    # -----------------------
    # 2. Create Agent(analyze email)
    # -----------------------

    #agent = CustomerAgent(API_KEY)
    agent = CustomerAgent()
    print("\nAgent created.")

    # -----------------------
    # 3.  Analyze email
    # -----------------------
    print("Analyzing email...")
    result = agent.analyze_email(email)

    print("AI result:")
    print(result)
    print("\n----test--result is printed-----------------")


    # -----------------------
    # 4.  Connect to  CRM
    # -----------------------
    print("\nConnecting to CRM...")
    crm = CRM()


    customer = result["customer"]
    print("\nCustomer info extracted from email:")
    print(customer)

    existing_customer = crm.find_customer(
        customer["email"]
    )


    # -----------------------
    # 5. Decision
    # -----------------------
    print("\nChecking if customer exists in CRM...")
    if existing_customer:

        print("\nExisting customer found.")

    else:

        print("\nNew customer.")

        crm.create_customer(customer)


    # -----------------------
    # 6. Answer
    # -----------------------

    print("\nSuggested response:")

    print(result["response_text"])


if __name__ == "__main__":
    main()