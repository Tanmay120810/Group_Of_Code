import os

print("Starting PARASHAR GUI")

# Function for user authentication
def authenticate_user():
    """
    Authenticate user by requesting a user ID and password.
    Returns:
        tuple: Contains user_id and password for further processing.
    """
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")
    print("\nWelcome to Parashar GUI!\n")
    return user_id, password

# Function for comparer software
def comparer_software():
    """
    Starts comparer software which allows the user to compare two numbers.
    """
    name = input("Enter your name: ")
    print(f"\nComparer software started for {name}")

    # Compare two numbers with input validation
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if a > b:
            print("First number is greater than the second number.")
        elif a < b:
            print("Second number is greater than the first number.")
        else:
            print("Both numbers are equal.")
    except ValueError:
        print("Invalid input! Please enter valid integers.")
    input("\nPress Enter to return to the main menu...")

# Function for print shop
def print_shop():
    """
    Simulates a print shop operation by allowing the user to enter data for printing.
    """
    print("Print Shop opened.")
    data_to_print = input("Enter your data to be printed: ")
    print(f"Your data: '{data_to_print}' will be printed on your hardware.")
    input("\nPress Enter to return to the main menu...")

# Function for calculator
def calculator():
    """
    Basic calculator that performs addition, subtraction, multiplication, and division.
    """
    print("\nCalculator")
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        op = input("Enter operation (+, -, *, /): ")
        
        if op == "+":
            print("Result:", x + y)
        elif op == "-":
            print("Result:", x - y)
        elif op == "*":
            print("Result:", x * y)
        elif op == "/":
            if y != 0:
                print("Result:", x / y)
            else:
                print("Error: Division by zero!")
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    input("\nPress Enter to return to the main menu...")

# Function for data entry
def data_entry():
    """
    Allows entry of client details and saves them to a text file on the desktop.
    """
    print("\nEnter your client details below:")
    name = input("Enter client name: ")
    age = input("Enter client age: ")
    mobile = input("Enter client mobile number: ")
    address = input("Enter client address: ")
    order = input("Enter your order: ")

    # Define the desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "Client_Data.txt")

    # Save the data to a text file on the desktop
    try:
        with open(file_path, "a") as file:
            file.write(f"Client Name: {name}\n")
            file.write(f"Client Age: {age}\n")
            file.write(f"Mobile Number: {mobile}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Order: {order}\n")
            file.write("-----\n")  # Separator between entries
        print(f"\nClient data has been saved to your desktop as 'Client_Data.txt'.")
    except Exception as e:
        print(f"Error saving the client data: {e}")

    input("\nPress Enter to return to the main menu...")

# Function for Parashar Word
def parashar_word():
    """
    Simple text editor that allows the user to enter a document and saves it to the desktop.
    """
    document = input("Type your document: ")
    print("\nDocument entered successfully.\n")
    print("Here is the content you entered in Parashar Word:\n")
    print(f"--- Start of Document ---\n{document}\n--- End of Document ---")

    # Define the desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "Parashar_Word_Document.txt")

    # Save the document to a text file on the desktop
    try:
        with open(file_path, "w") as file:
            file.write(document)
        print(f"\nYour document has been saved to your desktop as 'Parashar_Word_Document.txt'.")
    except Exception as e:
        print(f"Error saving the document: {e}")

    input("\nPress Enter to return to the main menu...")

# Function for system information
def system_info():
    """
    Displays basic system information.
    """
    print("\nSystem Information:")
    print("4GB RAM\n500GB Hard Drive\nOS: Parashar GUI\nSystem Name: Parashar System")
    print("Your PARASHAR GUI is not activated. Please activate it by entering the product key sent to your email.")
    input("\nPress Enter to return to the main menu...")

# Main function
def main():
    """
    Main function for the PARASHAR GUI application.
    Provides a menu for users to select various functionalities.
    """
    # User Authentication
    authenticate_user()

    # Loop for continuous operation selection
    while True:
        print("\nSelect an operation:")
        print("1. Comparer Software\n2. Print Shop\n3. Calculator\n4. Data Entry\n5. Parashar Word\n6. System Information\n7. Exit")

        operation = input("Enter the number of your selected operation: ")

        if operation == "1":
            comparer_software()
        elif operation == "2":
            print_shop()
        elif operation == "3":
            calculator()
        elif operation == "4":
            data_entry()
        elif operation == "5":
            parashar_word()
        elif operation == "6":
            system_info()
        elif operation == "7":
            print("\nThank you for using PARASHAR GUI. Goodbye! We will MEET SOON.")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 7.")

# Run the main function
if __name__ == "__main__":
    main()

# Our software is an operating system which can run on a device with 8MB RAM and 20MB ROM,
# providing a smooth experience and great performance. To purchase this OS, contact:
# Tanmay Prashar (Owner of Parashar Company)
# Mobile number: 9162309057
