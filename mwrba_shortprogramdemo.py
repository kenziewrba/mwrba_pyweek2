# Simple To-Do List App

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ '{task}' has been added to your list.")
    elif choice == "2":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    elif choice == "3":
        print("\nSelect a task to remove:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
        try:
            num = int(input("Enter task number: "))
            removed = tasks.pop(num - 1)
            print(f"❌ '{removed}' removed.")
        except (ValueError, IndexError):
            print("Invalid choice.")
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Please enter a number 1–4.")
