a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("Choose operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", a + b)

elif choice == 2:
    print("Result:", a - b)

elif choice == 3:
    print("Result:", a * b)

elif choice == 4:
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)

else:
    print("Invalid choice")
