import os
from dotenv import load_dotenv
import json
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
    print("----test--email is printed-------------------------------------")


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
    # result = agent.analyze_email(email)
    # result = json.loads(result)  # Convert the string result to a dictionary
    # print("AI result:test json is printed")
    # print(result)
    # customer = result["customer name"]
    # print("\n-----------test--result is printed--------------------------------")
    

    result = agent.analyze_email(email)

    print("\nRAW AI RESULT:")
    print(result)

    result = json.loads(result)

    print("\nParsed result:")
    print(result)

    #customer = result["customer_name"]
    customer = result

    print("\nCustomer info extracted from email:")
    print(customer)



    # -----------------------
    # 4.  Connect to  CRM
    # -----------------------
    print("\nConnecting to CRM...")
    # crm = CRM()


    # customer = result["customer_name"]
    # print("\nCustomer info extracted from email:")
    # print(customer)

    # existing_customer = crm.find_customer(
    #     customer["email"]
    # )
    print("\nConnecting to CRM...")

    crm = CRM()

    customer = result

    print("\nCustomer info extracted from email:")
    print(customer)

    print("\nCustomer name:")
    print(customer["customer_name"])

    print("\nLocation:")
    print(customer["location"])

    print("\nProblem:")
    print(customer["problem"])

    print("\nRequested appointment:")
    print(customer["requested_appointment"])

    print("\nUrgency:")
    print(customer["urgency"])

    print("\nCategory:")
    print(customer["category"])


    # -----------------------
    # 5. Decision
    # -----------------------
    print("\nChecking if customer exists in CRM...")
    # if existing_customer:

    #     print("\nExisting customer found.")

    # else:

    #     print("\nNew customer.")

    crm.create_customer(customer)


    # -----------------------
    # 6. Answer
    # -----------------------

    print("\nSuggested response:")
    print("\nAI analysis completed successfully.")
    print(result)


if __name__ == "__main__":
    main()