while True:
    print("\n🌡️ Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print(f"✅ {c}°C = {f}°F")

    elif choice == '2':
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"✅ {f}°F = {c}°C")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")