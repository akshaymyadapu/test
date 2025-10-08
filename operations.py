from database import get_connection
conn=get_connection()
cursor=conn.cursor()


def saving_account():
    Acc_number = input("Enter your account number: ")
    Name = input("Enter your name: ")
    pin_number = input("Enter your 4-digit pin number: ")
    welcome()

def Business_account():
    Business_name = input("Enter business name: ")
    Initial_balance = float(input("Enter the amount: "))
    welcome()

def welcome():
    print("Welcome to the bank")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    option = int(input("Choose an option: "))

    if option == 1:
        deposit()

    elif option == 2:
        withdraw()

    elif option == 3:
        check_balance()

    elif option == 4:
        exit()

    else:
        print("Invalid option")
        welcome()

def deposit():
    amount = float(input("Enter amount to deposit: "))
    print(f"Deposited {amount} successfully")
    welcome()

def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    print(f"Withdrew {amount} successfully")
    welcome()

def check_balance():
    print("Your balance is ")
    welcome()





