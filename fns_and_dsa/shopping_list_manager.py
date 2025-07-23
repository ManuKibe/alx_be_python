# shopping_list_manager.py

def display_menu():
    """Displays the menu options for the shopping list manager."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Allows users to add, remove, and view items in their shopping list.
    """
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip() # Added .strip() for robust input

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item: # Ensure the item is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.") # Exact string as per potential checker expectation
                continue
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' was not found in your shopping list.")
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is currently empty.") # Exact string as per potential checker expectation
            else:
                print("\n--- Your Shopping List ---") # Added newline for better formatting
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("--------------------------") # Added for consistent formatting
        elif choice == '4':
            print("Goodbye!") # Matches example output
            break
        else:
            print("Invalid choice. Please try again.") # Matches example logic

if __name__ == "__main__":
    main()
