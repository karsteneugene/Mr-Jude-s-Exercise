from Account import Account


class Customer:
    def __init__(self, firstName, lastName):
        self.firstname = firstName
        self.lastname = lastName
        self.account = Account()

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_account(self):
        return self.account

    def set_account(self, acct):
        self.account = acct
