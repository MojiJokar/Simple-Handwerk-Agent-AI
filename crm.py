import json
import os


class CRM:

    def __init__(self):

        self.file_path = "data/crm.json"
        # Make sure the data folder exists
        os.makedirs("data", exist_ok=True)

        
        # Make sure the CRM file exists
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)

### Test to check the file created or exist:

    print("Current directory:", os.getcwd())
    print("File path:", os.path.abspath("data/crm.json"))

    def get_customers(self):
        if not os.path.exists(self.file_path):
            return []

        if os.path.getsize(self.file_path) == 0:
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def find_customer(self, email):

        customers = self.get_customers()

        for customer in customers:

            if customer["email"] == email:
                return customer

        return None

    def create_customer(self, customer):
        customers = self.get_customers()

        customers.append(customer)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                customers,
                file,
                indent=4,
                ensure_ascii=False
            )

        return customer