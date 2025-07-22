def display_menu():
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

shopping_list = []

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        continue
    choice = int(choice)

    if choice == 1:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to list.")
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print(f"{item} not found.")
    elif choice == 3:
        print("Shopping List:", shopping_list)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
