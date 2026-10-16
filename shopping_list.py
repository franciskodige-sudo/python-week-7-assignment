shopping_list = []

while True:
    choice = input("add / remove / show / done: ").strip().lower()

    if choice == "add":
        item = input("Enter item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"{item} added to the list.")
        else:
            print("Please enter an item.")

    elif choice == "remove":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for item in shopping_list:
                print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")
