# --- Simple Hash Table Implementation ---
print("\n=== Hash Table Program ===")
m = int(input("Enter size of hash table: "))
table = [[] for _ in range(m)]

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        key = int(input("Enter key to insert: "))
        index = key % m
        if key not in table[index]:
            table[index].append(key)
            print(f"{key} inserted in bucket {index}.")
        else:
            print("Key already exists.")

    elif choice == "2":
        key = int(input("Enter key to search: "))
        index = key % m
        if key in table[index]:
            print(f"{key} found in bucket {index}.")
        else:
            print("Key not found.")

    elif choice == "3":
        key = int(input("Enter key to delete: "))
        index = key % m
        if key in table[index]:
            table[index].remove(key)
            print(f"{key} deleted from bucket {index}.")
        else:
            print("Key not found.")

    elif choice == "4":
        print("\n--- Hash Table ---")
        for i in range(m):
            print(f"Bucket {i}: {table[i]}")

    elif choice == "5":
        print("Exiting Hash Table program...")
        break

    else:
        print("Invalid choice! Try again.")


# --- Simple Stack Program with Undo and Redo ---
stack = []
history = []
redo_stack = []

print("\n=== Stack Program with Undo & Redo ===")

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Undo")
    print("6. Redo")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter value to push: ")
        stack.append(value)
        history.append(("push", value))
        redo_stack.clear()
        print(f"{value} pushed into stack.")

    elif choice == "2":
        if stack:
            popped = stack.pop()
            history.append(("pop", popped))
            redo_stack.clear()
            print(f"{popped} popped from stack.")
        else:
            print("Stack is empty.")

    elif choice == "3":
        if stack:
            print("Top element:", stack[-1])
        else:
            print("Stack is empty.")

    elif choice == "4":
        if stack:
            print("Stack elements:", stack)
        else:
            print("Stack is empty.")

    elif choice == "5":  # Undo
        if history:
            action, value = history.pop()
            if action == "push":
                stack.pop()
                redo_stack.append(("push", value))
            elif action == "pop":
                stack.append(value)
                redo_stack.append(("pop", value))
            print("Undo successful.")
        else:
            print("Nothing to undo.")

    elif choice == "6":  # Redo
        if redo_stack:
            action, value = redo_stack.pop()
            if action == "push":
                stack.append(value)
                history.append(("push", value))
            elif action == "pop":
                stack.pop()
                history.append(("pop", value))
            print("Redo successful.")
        else:
            print("Nothing to redo.")

    elif choice == "7":
        print("Exiting Stack program... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
