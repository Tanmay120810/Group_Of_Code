def homeopathy_medicine_recommender():
    print("=" * 50)
    print("WELCOME TO OUR HOMEOPATHY MEDICINE RECOMMENDER")
    print("=" * 50)
    print("This software is developed by MR. TANMAY PARASHAR")
    print("All rights reserved by Code with Parashar Company")
    print("=" * 50)
    print("don't take medicine from this refrence without consulting doctor\nit is just for idea to new coders")
    print("=" * 50)
    
    # Get user's name
    name = input("Please enter your name: ").strip()
    print(f"\nHello, {name}! We are here to help you find the right medicine for your illness.\n")
    
    # Display available options
    print("Please select your illness from the list below:")
    print("""
    1. Fever
    2. Gas
    3. Seasonal Illness
    4. Very High Fever
    5. Infections and Nerve Issues
    6. Body Pain or Injury
    7. Diabetes
    """)
    
    # Get user's choice
    illness = input("Enter the number corresponding to your illness: ").strip()
    
    # Suggest medicine based on the illness
    print("\nRecommended Medicine:")
    if illness == "1":
        print("Take Dulcamara 200CH.")
    elif illness == "2":
        print("Take Nux Vomica 200CH or Carbo Veg 200CH.")
    elif illness == "3":
        print("Take Rhus Tox 200CH.")
    elif illness == "4":
        print("Take Belladonna 200CH (2 drops for extreme conditions) or Rhus Tox 200CH (5 drops).")
    elif illness == "5":
        print("You should prefer Rhus Tox 1000CH (2 drops).")
    elif illness == "6":
        print("Take Arnica 200CH (3 drops).")
    elif illness == "7":
        print("Take Syzygium Jambolanum with water. Consult your doctor for the correct dosage.")
    else:
        print("Invalid selection. Please restart and choose a valid option.")
    
    print("\nThank you for using our Homeopathy Medicine Recommender!")
    print("Stay healthy and take care.")

# Run the program
homeopathy_medicine_recommender()
