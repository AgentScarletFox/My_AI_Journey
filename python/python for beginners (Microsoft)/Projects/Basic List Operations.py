numbers = []

while True:
    print("\n📊 List Operations Menu")
    print("1. Add Number")
    print("2. View List")
    print("3. Show Max, Min, Sum, Average")
    print("4. Sort List")
    print("5. Remove Number")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        num = float(input("Enter a number: "))
        numbers.append(num)
        print("✅ Number added!")

    elif choice == '2':
        print("📋 Current List:", numbers)

    elif choice == '3':
        if numbers:
            print("Max:", max(numbers))
            print("Min:", min(numbers))
            print("Sum:", sum(numbers))
            print("Average:", sum(numbers) / len(numbers))
        else:
            print("❌ List is empty.")

    elif choice == '4':
        numbers.sort()
        print("✅ List sorted:", numbers)

    elif choice == '5':
        num = float(input("Enter number to remove: "))
        if num in numbers:
            numbers.remove(num)
            print("🗑️ Removed!")
        else:
            print("❌ Number not found.")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice.")