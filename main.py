from todo import TodoManager

app = TodoManager()

while True:
    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        app.add_task()
    elif choice == "2":
        app.view_tasks()
    elif choice == "3":
        app.search_task()
    elif choice == "4":
        app.delete_task()
    elif choice == "5":
        app.save_tasks()
        print("Tasks saved.")
        break
    else:
        print("Invalid choice.")
