import json
import os


class CRM:

    def __init__(self, filename="data/crm.json"):

        self.filename = filename

        if not os.path.exists(self.filename):

            with open(self.filename, "w") as file:
                json.dump([], file)

### Test to check the file created or exist:
    import os

    print("Current directory:", os.getcwd())
    print("File path:", os.path.abspath("data/crm.json"))
    def get_customers(self):

        with open(self.filename, "r") as file:
            return json.load(file)

    def find_customer(self, email):

        customers = self.get_customers()

        for customer in customers:

            if customer["email"] == email:
                return customer

        return None

    def create_customer(self, customer):

        customers = self.get_customers()

        customers.append(customer)

        with open(self.filename, "w") as file:

            json.dump(
                customers,
                file,
                indent=4,
                ensure_ascii=False
            )

        return customer