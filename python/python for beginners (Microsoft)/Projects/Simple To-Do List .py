# To-Do List with File Storage

FILE_NAME = "tasks.txt"

# Load tasks from file
try:
    with open(FILE_NAME, "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

while True:
    print("\n📋 To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        save_tasks()
        print("✅ Task saved!")

    elif choice == '2':
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == '3':
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()
            print(f"🗑️ Removed: {removed}")
        else:
            print("❌ Invalid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice.")