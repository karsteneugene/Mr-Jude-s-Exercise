from Customer import Customer


class Bank:
    number_of_customers = 0

    def __init__(self, bank_name, customers):
        self.bank_name = bank_name
        self.customers = customers

    def add_customer(self, f: str, l: str):
        self.customers.append(Customer(f, l))
        self.number_of_customers += 1

    def get_number_of_customers(self):
        return self.number_of_customers

    def get_customer(self, index: int):
        return self.customers[index]
