
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("THESE ARE THE OPERATORS")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

Operator = int(input("Choose a number from the list to perform an operation: "))

if Operator == 1:
    print("The sum is " + str(num1 + num2))
elif Operator == 2:
    print("The difference is " + str(num1 - num2))
elif Operator == 3:
    print("The product is " + str(num1 * num2))
elif Operator == 4:
    print("The Quotient is " + str(num1 / num2))
else:
    print("Enter a valid input!!!")
