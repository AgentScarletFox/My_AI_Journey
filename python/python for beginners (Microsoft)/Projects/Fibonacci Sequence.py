def fibonacci(n):
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

while True:
    user_input = input("Enter number of terms (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    
    if not user_input.isdigit():
        print("❌ Please enter a valid positive number.")
        continue
    
    n = int(user_input)
    result = fibonacci(n)
    
    print("✅ Fibonacci sequence:", result)
    print("-" * 30)