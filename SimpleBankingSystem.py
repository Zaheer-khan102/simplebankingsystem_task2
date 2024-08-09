class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Successful. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance. Please try again.")
        else:
            self.balance -= amount
            print(f"Withdrawal Successful. New balance is {self.balance}")

    def check_balance(self):
        print(f"Account balance is {self.balance}")


def main():
    account = BankAccount("John Doe", 1000)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()