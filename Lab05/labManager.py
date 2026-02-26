
# Author: Perfect Makuwerere
# Date: 02/24/2026
# Description: A program that manages equipments in a lab

laboratory_inventory = []
MAX_CAPACITY = 5

running = True

print("Welcome to the Laboratory Equipment Manager!")

while running:
    print("\n--- Main Menu ---")
    print("1. Add Equipment")
    print("2. Remove Equipment")
    print("3. Display Current Equipment")
    print("4. Leave the Laboratory Manager")
    
    choice = input("Select an option (1-4): ")

    if choice == "1":
        if len(laboratory_inventory) >= MAX_CAPACITY:
            print("Error: The laboratory is at full capacity (5 items). Cannot add more.")
        else:
            new_item = input("Enter the name of the equipment to add: ")
            laboratory_inventory.append(new_item)
            print(f"Success: '{new_item}' has been added to the inventory.")

    elif choice == "2":
        item_to_remove = input("Enter the name of the equipment to remove: ")
        
        if item_to_remove in laboratory_inventory:
            laboratory_inventory.remove(item_to_remove)
            print(f"Success: '{item_to_remove}' has been removed.")
        else:
            print(f"Error: '{item_to_remove}' was not found in the inventory.")


    elif choice == "3":
        if not laboratory_inventory:
            print("The laboratory is currently empty.")
        else:
            print("Current Inventory: ", end="")
            for item in laboratory_inventory:
                print(f"[{item}]", end=" ")
            print() 

    elif choice == "4":
        print("Thank you for using the Lab Manager. Good luck on your journey of discovery!")
        running = False

    else:
        print("Invalid selection. Please choose a number between 1 and 4.")

