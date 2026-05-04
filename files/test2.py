import datetime


# ---------------- BANK SYSTEM ----------------
class BankAccount:
    account_counter = 1000

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.account_number = BankAccount.account_counter
        self.transactions = []
        BankAccount.account_counter += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"{datetime.datetime.now()} - Deposited {amount}")
            print(f"Deposited {amount}. Balance: {self.balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(f"{datetime.datetime.now()} - Withdrew {amount}")
            print(f"Withdrew {amount}. Balance: {self.balance}")

    def show_balance(self):
        print(f"Account Balance: {self.balance}")

    def show_transactions(self):
        print("\nTransaction History:")
        for t in self.transactions:
            print(t)


# ---------------- INSURANCE SYSTEM ----------------
class InsurancePolicy:
    def __init__(self, policy_type, premium):
        self.policy_type = policy_type
        self.premium = premium
        self.active = False
        self.claims = []

    def activate(self, account):
        if account.balance >= self.premium:
            account.withdraw(self.premium)
            self.active = True
            print(f"{self.policy_type} policy activated.")
        else:
            print("Not enough balance.")

    def make_claim(self, amount):
        if not self.active:
            print("Policy not active.")
        else:
            self.claims.append(amount)
            print(f"Claim of {amount} recorded.")

    def show_claims(self):
        print("Claims History:")
        for c in self.claims:
            print(c)


# ---------------- USER SYSTEM ----------------
class Customer:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(name)
        self.policies = []

    def add_policy(self, policy):
        self.policies.append(policy)


# ---------------- MAIN SYSTEM ----------------
class BankInsuranceSystem:
    def __init__(self):
        self.customers = {}

    def create_customer(self):
        name = input("Enter customer name: ")
        if name in self.customers:
            print("Customer already exists.")
        else:
            self.customers[name] = Customer(name)
            print("Customer created successfully.")

    def select_customer(self):
        name = input("Enter customer name: ")
        return self.customers.get(name, None)

    def run(self):
        while True:
            print("\n--- MAIN MENU ---")
            print("1. Create Customer")
            print("2. Access Customer")
            print("3. Exit")

            choice = input("Choice: ")

            if choice == "1":
                self.create_customer()

            elif choice == "2":
                customer = self.select_customer()
                if customer:
                    self.customer_menu(customer)
                else:
                    print("Customer not found.")

            elif choice == "3":
                print("Exiting system.")
                break

            else:
                print("Invalid choice.")

    def customer_menu(self, customer):
        while True:
            print(f"\n--- {customer.name}'s MENU ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. View Transactions")
            print("5. Buy Insurance")
            print("6. View Policies")
            print("7. Back")

            choice = input("Choice: ")

            if choice == "1":
                amount = float(input("Amount: "))
                customer.account.deposit(amount)

            elif choice == "2":
                amount = float(input("Amount: "))
                customer.account.withdraw(amount)

            elif choice == "3":
                customer.account.show_balance()

            elif choice == "4":
                customer.account.show_transactions()

            elif choice == "5":
                self.buy_policy(customer)

            elif choice == "6":
                self.policy_menu(customer)

            elif choice == "7":
                break

            else:
                print("Invalid choice.")

    def buy_policy(self, customer):
        print("\nInsurance Types:")
        print("1. Health (Premium: 200)")
        print("2. Car (Premium: 300)")
        print("3. Life (Premium: 500)")

        choice = input("Select: ")

        if choice == "1":
            policy = InsurancePolicy("Health", 200)
        elif choice == "2":
            policy = InsurancePolicy("Car", 300)
        elif choice == "3":
            policy = InsurancePolicy("Life", 500)
        else:
            print("Invalid option.")
            return

        policy.activate(customer.account)
        if policy.active:
            customer.add_policy(policy)

    def policy_menu(self, customer):
        if not customer.policies:
            print("No policies found.")
            return

        for i, p in enumerate(customer.policies):
            print(f"{i+1}. {p.policy_type} (Active: {p.active})")

        choice = int(input("Select policy: ")) - 1

        if 0 <= choice < len(customer.policies):
            policy = customer.policies[choice]

            while True:
                print(f"\n--- {policy.policy_type} POLICY ---")
                print("1. Make Claim")
                print("2. View Claims")
                print("3. Back")

                opt = input("Choice: ")

                if opt == "1":
                    amount = float(input("Claim amount: "))
                    policy.make_claim(amount)

                elif opt == "2":
                    policy.show_claims()

                elif opt == "3":
                    break

                else:
                    print("Invalid option.")
        else:
            print("Invalid selection.")


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    system = BankInsuranceSystem()
    system.run()