import json
import os

# File paths for data storage
INVENTORY_FILE = "inventory.json"
CUSTOMERS_FILE = "customers.json"

# Functions to handle JSON file operations
def load_data(file_path, default_data):
    """Load data from a JSON file or return default data."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return default_data

def save_data(file_path, data):
    """Save data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Load inventory and customer data
inventory = load_data(INVENTORY_FILE, {
    "haldi": {"price": 170, "quantity": 100},
    "dhaniya": {"price": 180, "quantity": 50},
    "mix masala": {"price": 250, "quantity": 30},
    "mirchi": {"price": 350, "quantity": 20},
})

customers = load_data(CUSTOMERS_FILE, {})

# Branding and UI
def print_header():
    """Display the professional branding header."""
    print("=" * 50)
    print("🏪  Moni Food Products Management System  🏪")
    print("✨ Quality is our priority ✨".center(50))
    print("📞 Contact: +91 9304289399".center(50))
    print("© 2024 Moni Food Products. All rights reserved.".center(50))
    print("=" * 50)

def print_footer():
    """Display a thank-you message with branding."""
    print("\n" + "=" * 50)
    print("🙏 Thank you for using Moni Food Products Management System! 🙏")
    print("🏪 Moni Food Products: Trust in Quality.")
    print("=" * 50)

# Login process
print_header()
while True:
    password = input("🔑 Please enter your password to continue: ")
    if password == "moni":
        print("\n✅ Login successful! Welcome to Moni Food Products.")
        break
    else:
        print("❌ Incorrect password. Please try again.\n")

# Main menu
while True:
    print("\n🔹 Main Menu 🔹")
    print("1️⃣ View all item details")
    print("2️⃣ Change item price")
    print("3️⃣ Generate bill (for multiple items)")
    print("4️⃣ Update available quantity")
    print("5️⃣ Add a customer")
    print("6️⃣ View customer transaction history")
    print("7️⃣ Exit the app")
    
    choice = input("\nPlease choose an option (1/2/3/4/5/6/7): ").strip()
    
    if choice == "1":
        # Show all item details
        print("\n📋 Available items and their details:")
        print("===================================")
        for item, details in inventory.items():
            print(f"* {item.capitalize()} - ₹{details['price']} per kg, Available: {details['quantity']} kg")
        print("===================================")
    
    elif choice == "2":
        # Option to change item price
        item_to_update = input("🔄 Enter the name of the item to update its price: ").strip().lower()
        if item_to_update in inventory:
            try:
                new_price = float(input(f"💰 Enter the new price for {item_to_update.capitalize()} (₹): "))
                inventory[item_to_update]["price"] = new_price
                save_data(INVENTORY_FILE, inventory)
                print(f"✅ Price of {item_to_update.capitalize()} successfully updated.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
        else:
            print("❌ Item not available in the inventory.")
    
    elif choice == "3":
        # Generate bill for multiple items
        print("\n🛒 Billing process started...")
        total_bill = 0
        customer_name = input("👤 Enter the customer's name: ").strip()
        if customer_name not in customers:
            print(f"🔔 Customer '{customer_name}' not found. Please add them first (Option 5).")
            continue
        
        customer_history = customers[customer_name]
        while True:
            item_name = input("\nEnter the name of the item (or type 'done' to finish): ").strip().lower()
            if item_name == "done":
                break
            if item_name in inventory:
                try:
                    available_quantity = inventory[item_name]["quantity"]
                    print(f"🛒 {item_name.capitalize()} has {available_quantity} kg available.")
                    quantity = float(input(f"How many kilograms of {item_name.capitalize()} would you like to sell? "))
                    if quantity <= available_quantity:
                        item_total = inventory[item_name]["price"] * quantity
                        inventory[item_name]["quantity"] -= quantity
                        total_bill += item_total
                        print(f"✅ Added ₹{item_total:.2f} to the bill for {item_name.capitalize()}.")
                        # Record transaction in customer history
                        customer_history.append({
                            "item": item_name.capitalize(),
                            "quantity": quantity,
                            "total_price": item_total
                        })
                        save_data(INVENTORY_FILE, inventory)
                        save_data(CUSTOMERS_FILE, customers)
                    else:
                        print("❌ Requested quantity not available. Please enter a smaller amount.")
                except ValueError:
                    print("❌ Invalid quantity entered. Please enter a valid number.")
            else:
                print("❌ Item not available in the inventory.")
        
        # Print final bill
        print("\n🧾 Your final bill:")
        print("===================================")
        print(f"Total Payable Amount: ₹{total_bill:.2f}")
        print("===================================")
        print_footer()
    
    elif choice == "4":
        # Update available quantity of an item
        print("\n📦 Update Available Quantity")
        item_to_update = input("🔄 Enter the name of the item to update its quantity: ").strip().lower()
        if item_to_update in inventory:
            try:
                additional_quantity = float(input(f"📦 Enter the quantity to add for {item_to_update.capitalize()} (kg): "))
                if additional_quantity >= 0:
                    inventory[item_to_update]["quantity"] += additional_quantity
                    save_data(INVENTORY_FILE, inventory)
                    print(f"✅ {item_to_update.capitalize()} now has {inventory[item_to_update]['quantity']} kg available.")
                else:
                    print("❌ Quantity cannot be negative.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
        else:
            print("❌ Item not available in the inventory.")
    
    elif choice == "5":
        # Add a customer
        customer_name = input("👤 Enter the new customer's name: ").strip()
        if customer_name in customers:
            print(f"🔔 Customer '{customer_name}' already exists.")
        else:
            customers[customer_name] = []
            save_data(CUSTOMERS_FILE, customers)
            print(f"✅ Customer '{customer_name}' successfully added.")
    
    elif choice == "6":
        # View customer transaction history
        customer_name = input("👤 Enter the customer's name to view their transaction history: ").strip()
        if customer_name in customers:
            history = customers[customer_name]
            if history:
                print(f"\n🧾 Transaction history for {customer_name}:")
                print("===================================")
                for record in history:
                    print(f"* Item: {record['item']}, Quantity: {record['quantity']} kg, Total Price: ₹{record['total_price']:.2f}")
                print("===================================")
            else:
                print(f"🔔 No transactions found for '{customer_name}'.")
        else:
            print(f"❌ Customer '{customer_name}' not found.")
    
    elif choice == "7":
        # Exit
        print_footer()
        break
    
    else:
        print("❌ Invalid option. Please choose a valid option.")
