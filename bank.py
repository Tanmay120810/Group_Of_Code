import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Email details
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password
RECIPIENT_EMAIL = "maaagency850@gmail.com"

# File path for storing account data
DATA_FILE = "accounts_data.json"

# Load account data from file if it exists
def load_account_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        return {}
    except Exception as e:
        print(f"Error loading account data: {e}")
        return {}

# Save account data to file
def save_account_data():
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(accounts_data, file)
    except Exception as e:
        print(f"Error saving account data: {e}")

# Send email notification
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Notification email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Initialize account data
accounts_data = load_account_data()

# Main interface
#NAME PLATE
print("**********************************")
print("*Welcome to Parashar Bank of India*")
print("***********************************")

def main_menu():
    print("\nMain Menu:")
    print("1. New Account - Open a new account")
    print("2. Balance Check - Check account balance")
    print("3. Deposit - Deposit funds into your account")
    print("4. Withdraw - Withdraw funds from your account")
    print("5. Account Statement - View your transaction history")
    print("6. Close Account - Close an existing account")
    print("7. Loan - Get details on available loans")
    print("8. Exit - Leave the program")

def get_account_info():
    account_number = input("Enter Account Number: ")
    holder_name = input("Enter Account Holder Name: ")
    return account_number, holder_name

def validate_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def new_account():
    account_number = input("Enter New Account Number: ")
    holder_name = input("Enter Account Holder Name: ")
    pin = input("Set a 4-digit PIN for secure access: ")
    initial_balance = validate_positive_float("Enter Initial Balance: ₹")
    mobile_number = input("Enter Mobile Number: ")
    auto_email = input("Would you like automatic email notifications for all transactions? (yes/no): ").strip().lower() == "yes"

    accounts_data[account_number] = {
        "holder_name": holder_name,
        "pin": pin,
        "balance": initial_balance,
        "transaction_history": [],
        "auto_email": auto_email
    }
    save_account_data()
    print(f"\nAccount created successfully! Welcome to Parashar Bank, {holder_name}!")

def authenticate(account_number):
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if accounts_data[account_number]["pin"] == pin:
            return True
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempts left.")
    print("Too many failed attempts. Returning to the main menu.")
    return False
#CODE WITH PARASHAR
def balance_check():
    account_number, holder_name = get_account_info()
    account = accounts_data.get(account_number)
    if account and account["holder_name"].lower() == holder_name.lower() and authenticate(account_number):
        print(f"\nThe balance for account {account_number} is: ₹{account['balance']}")
    else:
        print("Invalid account or PIN You have only 3 attempts left.\nPlease try again.")

def deposit():
    account_number, holder_name = get_account_info()
    account = accounts_data.get(account_number)
    if account and account["holder_name"].lower() == holder_name.lower() and authenticate(account_number):
        amount = validate_positive_float("Enter the Amount to Deposit: ₹")
        account["balance"] += amount
        transaction = f"Deposited ₹{amount} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        account["transaction_history"].append(transaction)
        save_account_data()
        print(f"\n₹{amount} has been successfully deposited to account {account_number}.\nCurrent Balance: ₹{account['balance']}")
        
        if account["auto_email"] or input("Would you like an email notification for this deposit? (yes/no): ").strip().lower() == "yes":
            send_email("Deposit Notification", f"₹{amount} has been deposited to account {account_number}. Current Balance: ₹{account['balance']}")
    else:
        print("Invalid account or PIN. Please try again.")

def withdraw():
    account_number, holder_name = get_account_info()
    account = accounts_data.get(account_number)
    if account and account["holder_name"].lower() == holder_name.lower() and authenticate(account_number):
        amount = validate_positive_float("Enter the Amount to Withdraw: ₹")
        if amount <= account["balance"]:
            account["balance"] -= amount
            transaction = f"Withdrew ₹{amount} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            account["transaction_history"].append(transaction)
            save_account_data()
            print(f"\n₹{amount} has been successfully withdrawn from account {account_number}.\nCurrent Balance: ₹{account['balance']}")
            
            if account["auto_email"] or input("Would you like an email notification for this withdrawal? (yes/no): ").strip().lower() == "yes":
                send_email("Withdrawal Notification", f"₹{amount} has been withdrawn from account {account_number}. Current Balance: ₹{account['balance']}")
        else:
            print("Insufficient funds. Please enter a lesser amount.")
    else:
        print("Invalid account or PIN. Please try again.")

def account_statement():
    account_number, holder_name = get_account_info()
    account = accounts_data.get(account_number)
    if account and account["holder_name"].lower() == holder_name.lower() and authenticate(account_number):
        print("\nTransaction History:")
        for transaction in account["transaction_history"]:
            print(transaction)
    else:
        print("Invalid account or PIN. Please try again.")

def close_account():
    account_number, holder_name = get_account_info()
    if account_number in accounts_data and accounts_data[account_number]["holder_name"].lower() == holder_name.lower() and authenticate(account_number):
        reason = input("Please tell us why you're closing the account: ")
        del accounts_data[account_number]
        save_account_data()
        print(f"\nWe're sorry to see you go, {holder_name}. Your account has been closed.")
    else:
        print("Invalid account or PIN. Please try again.")

def loan():
    print("\nParashar Bank offers an overdraft facility with a limit up to ₹50 lakhs.")
    print("Please visit your nearest branch or contact customer service to open an overdraft account.")
    print("Repayment terms are flexible, with options for monthly or yearly payments.")

while True:
    main_menu()
    operation = input("Enter the number of your selected operation: ")

    if operation == "1":
        new_account()
    elif operation == "2":
        balance_check()
    elif operation == "3":
        deposit()
    elif operation == "4":
        withdraw()
    elif operation == "5":
        account_statement()
    elif operation == "6":
        close_account()
    elif operation == "7":
        loan()
    elif operation == "8":
        print("\nThank you for using Parashar Bank of India. Goodbye!")
        break
    else:
        print("Invalid selection. Please try again.")

    if input("\nWould you like to return to the main menu? (yes/no): ").strip().lower() != 'yes':
        print("\nThank you for using Parashar Bank of India. Goodbye!")
        break
    #************************************************
    #*this software is developed by Tanmay parashar  *
    #*************************************************

