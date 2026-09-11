import os
from dotenv import load_dotenv
import json
from agent import CustomerAgent
from crm import CRM
from email_service import get_new_email


load_dotenv()



def main():

    # 1. receive email

    email = get_new_email()

    # 2. Create Agent(analyze email)
    agent = CustomerAgent()
    print("\nnew Agent created : ---------------------------------------------------")

    # 3.  Analyze email
    print("Analyzing email...")

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
    print("\nConnecting to CRM...==>>>>>>>>>>>>>>>>>>>")

    crm = CRM()

    customer = result
    
    # print("\nsender's email: ")
    # print(customer["customer_email"])
    # print("\nsender's Name: ")
    # print(customer["customer_name"])
    
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
    # print("\nChecking if customer exists in CRM...")
    # crm.create_customer(customer)
    
    print("\nChecking if customer exists in CRM...")

    #existing_customer = crm.find_customer(customer["customer_name"])
    existing_customer = crm.find_customer(customer["location"])

    if existing_customer:
        print("\nCustomer already exists in CRM.")
        print("Updating customer...")

        crm.update_customer(
            customer["location"],
            customer
        )

        print("Customer updated successfully.")

    else:
        print("\nCustomer does not exist in CRM.")
        print("Creating new customer...")

        crm.create_customer(customer)

        print("Customer created successfully.")
    
    
    # -----------------------
    # 6. Answer
    # -----------------------

    print("\nSuggested response:")
    print("\nAI analysis completed successfully.")
    print(result)


if __name__ == "__main__":
    main()