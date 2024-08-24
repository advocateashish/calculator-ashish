# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to print the calculator menu
def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

# Main program
while True:
    menu()
    
    # Take input from the user
    choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

    if choice == 'q':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")

        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")

        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")

        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input! Please enter a valid option.")
