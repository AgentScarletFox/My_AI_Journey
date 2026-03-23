# Simple Notes Saver

FILE_NAME = "notes.txt"

while True:
    print("\n📝 Notes App")
    print("1. Write Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        note = input("Enter your note: ")
        with open(FILE_NAME, "a") as file:
            file.write(note + "\n")
        print("✅ Note saved!")

    elif choice == '2':
        try:
            with open(FILE_NAME, "r") as file:
                print("\n📄 Your Notes:")
                print(file.read())
        except FileNotFoundError:
            print("❌ No notes found.")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice.")