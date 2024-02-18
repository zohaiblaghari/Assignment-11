def verify_pin(correct_pin):
    attempts = 3
    while attempts > 0:
        pin = input("Enter your pin:")
        if pin == correct_pin:
            return True
        else:
            print("Incorrect PIN. please try again.")
            attempts -= 1
    print("Too many incorrect attempts. your card is blocked.")
    return False

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw:"))
    if amount <= balance:
        balance -= amount
        print(f"Withdrwal successful, Remaining balance: {balance}")
    else:
        print("Insufficient balance.")

def main():
    correct_pin = "1234"
    balance = 1000.00

    if verify_pin(correct_pin):
        print("Welcome to the ATM!")
        print("1. Withdraw Money\n2.Exit")
        option = input("Enter your choice:")
        
        if option == "1":
            withdraw(balance)
        elif option == "2":
            print("Thank you for using the ATM. Goodbye!")
        else:
            print("Invalid option.")
    else:
        print("Please contact your bank for assistance.")

if __name__ == "__main__":
    main()