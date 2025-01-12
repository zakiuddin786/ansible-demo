import random

class BankAccount:
    def __init__(self, owner, balance, address, contact_details, identity_proof, owner_pic, nominee_name ):
        self.owner = owner
        self.__balance = balance
        self.__address = address
        self.__contact_details = contact_details
        self.__identity_proof = identity_proof
        self.owner_pic = owner_pic
        self.__account_id = "not generated"

    def create_account(self):
        # Check Whether the user exists in DB or not and accordingly take the next steps
        self.account_id = self.__generate_account_number(8, 12)
        print(f"{self.owner} Account created successfully! with id {self.account_id}")
        # Logic to update this entry in the DB
    
    def deposit_money(self, amount):
        print(f"Depositing {amount} in {self.owner} Account")
        self.__balance +=amount

        print(f"Deposited successfully, Updated Balance  is {self.__balance}")

    def withdraw_money(self, amount):
        print(f"Trying to withdraw {amount} from {self.owner} Account")
        if amount <= self.__balance:
            self.__balance -=amount
            print(f"Withdrawal successful, Updated Balance  is {self.__balance}")

        else:
            print("Insufficient funds !")

    def get_balance(self):
        return self.__balance # Controlled Access

    def __generate_account_number(self, starting_series, account_digits):
        account_number = "".join(str(random.randint(0,9)) for _ in  range(account_digits-1))
        final_account_number = f"{starting_series}{account_number}"
        return final_account_number



ashutosh_account = BankAccount("Ashutosh", 8500000, "Varanasi", "100", "aadhar", "good_pic", "nayan")

ashutosh_account.create_account()
ashutosh_account.deposit_money(10000000)

# print(ashutosh_account.__balance) Will throw an error of attr not found

print(f"{ashutosh_account.owner} balance is {ashutosh_account.get_balance()}")

ashutosh_account.withdraw_money(9000000)

nayan_account = BankAccount("Nayan", 20000000, "Dubai", "102", "aadhar", "good_pic", "ashutosh")
nayan_account.create_account()
nayan_account.deposit_money(100000000)
print(f"{nayan_account.owner} balance is {nayan_account.get_balance()}")

nayan_account.withdraw_money(30000000)


