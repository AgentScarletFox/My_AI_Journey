def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    user_input = input("Enter a non-negative integer (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        print("Exiting the program. Goodbye!")
        break
    
    if not user_input.isdigit():
        print("❌ Invalid input. Please enter a non-negative integer.")
        continue
    
    num = int(user_input)
    print(f"✅ The factorial of {num} is {factorial(num)}.\n")