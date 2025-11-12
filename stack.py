stack = []
history = []
redo_stack = []
while True:
    print("\n--- Stack Operations ---")
    print("1. Push")
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

    elif choice == "5":   
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

    elif choice == "6":  
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
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")