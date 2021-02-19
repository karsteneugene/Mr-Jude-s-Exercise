from Account import Account
from Customer import Customer
from Bank import Bank


def main():
    customers = []
    bca = Bank('BCA', customers)
    default = Account(0)

    def interaction():
        print('Welcome!\nWhat would you like to do today?')
        user_input = input('1. Create Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Exit\n--> ')

        if user_input == '1':
            firstname = input('\nEnter your first name: ')
            lastname = input('Enter your last name: ')
            bca.add_customer(firstname, lastname)
            bca.get_customer(len(customers)-1).set_account(Account(50000))
            print('\nAccount successfully created with a balance of 50000!\n')
            interaction()

        elif user_input == '2':

            if len(customers) == 0:
                print(f'\nHere is your current balance: {default.get_balance()}\n')
            else:
                print(f'\nHere is your current balance: {bca.get_customer(len(customers)-1).get_account().get_balance()}\n')
            interaction()

        elif user_input == '3':
            amt_to_deposit = int(input('\nEnter the amount to deposit: '))

            if len(customers) == 0:
                result = default.deposit(amt_to_deposit)
                if result is True:
                    print('\nTransaction Successful!\n')
                else:
                    print('\nTransaction Unsuccessful!\n')

            else:
                result = bca.get_customer(len(customers)-1).get_account().deposit(amt_to_deposit)
                if result is True:
                    print('\nTransaction Successful!\n')
                else:
                    print('\nTransaction Unsuccessful!\n')
            interaction()

        elif user_input == '4':
            amt_to_withdraw = int(input('\nEnter the amount to withdraw: '))

            if len(customers) == 0:
                result = default.withdraw(amt_to_withdraw)
                if result is True:
                    print('\nTransaction Successful!\n')
                else:
                    print('\nTransaction Unsuccessful!\n')

            else:
                result = bca.get_customer(len(customers)-1).get_account().withdraw(amt_to_withdraw)
                if result is True:
                    print('\nTransaction Successful!\n')
                else:
                    print('\nTransaction Unsuccessful!\n')
            interaction()

        elif user_input == '5':
            print('\nThank you for trusting us!\nSee you again soon!')

    interaction()


if __name__ == "__main__":
    main()
