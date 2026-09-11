# Simple-Handwerk-Agent-AI
An AI agent for skilled-trade companies (Handwerk) that reads customer emails, registers customers in the CRM, and categorizes new requests.


**Email → AI Agent → Analysis → CRM → Calendar → Response → Human Approval → Send**

# Handwerk AI Agent

An AI-powered customer service agent for handling incoming service requests for a handcraft/trades business.

The project demonstrates how an AI agent can read an incoming customer email, extract structured information about the customer and their service request, and interact with a simple CRM system to either create a new customer or update an existing customer.

## Project Overview

The agent follows this workflow:

```text
Incoming Email
      ↓
Email Service
      ↓
AI Agent
      ↓
Extract Customer Information
      ↓
CRM Check
      ↓
 ┌───────────────┐
 │ Customer      │
 │ already exists│
 └───────┬───────┘
         │
    YES  │  NO
     ↓       ↓
  UPDATE   CREATE
     \       /
      \     /
       ↓   ↓
    CRM Database
```

## Main Features

* Receive incoming customer emails
* Analyze email content using an AI model
* Extract structured customer information
* Identify the customer's:

  * Name
  * Location
  * Problem
  * Requested appointment
  * Urgency
  * Service category
* Check whether the customer already exists in the CRM
* Update an existing customer instead of creating a duplicate
* Create a new customer when no existing customer is found
* Store customer information in a JSON-based CRM
* Generate a structured AI response

## Project Structure

```text
Handwerk-AI-agent/
│
├── main.py
├── crm.py
├── email_service.py
│
├── data/
│   └── crm.json
│
├── .env
├── .gitignore
└── README.md
```

### `main.py`

The main application entry point.

It coordinates the complete workflow:

1. Gets a new email from the email service
2. Sends the email content to the AI agent
3. Parses the AI response
4. Extracts customer information
5. Connects to the CRM
6. Checks whether the customer already exists
7. Updates the customer if they already exist
8. Creates a new customer if they do not exist
9. Displays the AI analysis/result

Example decision logic:

```python
existing_customer = crm.find_customer(
    customer["customer_name"]
)

if existing_customer:
    crm.update_customer(
        customer["customer_name"],
        customer
    )
else:
    crm.create_customer(customer)
```

### `email_service.py`

Provides the incoming email used by the application.

For the current exercise, the email is simulated with a Python function rather than retrieved from a real email provider.

Example:

```python
def get_new_email():
    return """
    Hi,

    my air conditioner is broken.
    I live in Darmstadt.

    Can you come on Sunday?

    Thanks

    Andrew Kamel
    """
```

This makes it possible to develop and test the AI agent without connecting to a real email server.

### `crm.py`

Contains the CRM functionality.

The CRM is responsible for managing customer records stored in `data/crm.json`.

Main operations include:

* `get_customers()` – loads customers from the JSON file
* `find_customer()` – searches for an existing customer
* `create_customer()` – creates a new customer
* `update_customer()` – updates an existing customer

The important business rule is:

```text
Customer exists → Update
Customer does not exist → Create
```

This prevents duplicate customer records.

### `data/crm.json`

Acts as the project's simple local CRM database.

Customer records are stored as JSON objects.

Example:

```json
[
    {
        "customer_name": "Andrew Kamel",
        "location": "Darmstadt",
        "problem": "air conditioner is broken",
        "requested_appointment": "Sunday",
        "urgency": "normal",
        "category": "air conditioning repair"
    }
]
```

For this exercise, the customer name is used to identify an existing customer because the simulated email does not provide a sender email address.

In a production system, a unique identifier such as an email address, phone number, or CRM customer ID would be preferable.

## AI Customer Information

The AI converts unstructured email text into structured data.

For example, from:

```text
My air conditioner is broken.
I live in Darmstadt.
Can you come on Sunday?
Thanks,
Andrew Kamel
```

the AI extracts:

```json
{
    "customer_name": "Andrew Kamel",
    "location": "Darmstadt",
    "problem": "air conditioner is broken",
    "requested_appointment": "Sunday",
    "urgency": "normal",
    "category": "air conditioning repair"
}
```

This structured information can then be used by the CRM and future business logic.

## Technologies

* Python
* AI / LLM API
* JSON
* File-based CRM
* Environment variables for configuration

## How the CRM Logic Works

The project is designed to avoid creating duplicate customers.

When a new email is received:

```text
1. Extract customer information
2. Search CRM for the customer
3. If customer exists:
       Update existing record
4. Otherwise:
       Create new record
```

This separates the responsibilities between the application and the CRM:

* `main.py` controls the workflow and business decision
* `crm.py` handles CRM operations
* `email_service.py` provides incoming emails
* `crm.json` stores customer data

## Example

Input email:

```text
Hi,

my air conditioner is broken.
I live in Darmstadt.

Can you come on Sunday?

Thanks,
Andrew Kamel
```

AI result:

```text
Customer: Andrew Kamel
Location: Darmstadt
Problem: Air conditioner is broken
Appointment: Sunday
Urgency: Normal
Category: Air conditioning repair
```

CRM:

```text
Checking if customer exists in CRM...

Customer already exists in CRM.
Updating customer...

Customer updated successfully.
```

If the customer does not exist:

```text
Checking if customer exists in CRM...

Customer does not exist in CRM.
Creating new customer...

Customer created successfully.
```

## Future Improvements

Possible improvements for a production-ready version include:

* Connect to a real email provider
* Use the sender's email address as the customer identifier
* Replace the JSON CRM with a real database
* Add customer IDs
* Store appointment history
* Add automatic appointment scheduling
* Generate and send automatic email replies
* Add validation for AI-generated data
* Add error handling and logging
* Add tests
* Add a web interface for CRM management
* Add authentication and secure API key management

## Purpose

This project is a learning project demonstrating how AI agents can connect unstructured customer communication with structured business processes and CRM operations.


