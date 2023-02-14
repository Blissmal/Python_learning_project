# functions
def emobilis():
    print("This is my first function")


emobilis()


# Function to calculate the area of a square
def calculate_square():
    x = 5
    y = 6
    print("The area is " + str(x * y))


calculate_square()


# Function to display names and age
def majina(f_name, l_name, age):
    print(f_name + l_name + age)


majina("Erick ", "Were ", "19")


# Function to calculate area of a circle
def CircleArea(r):
    pi = 22/7
    # r = int(input("Enter the radius: "))
    print("The area is " + str(pi * r))


CircleArea(7)


# Function to display a maximum value
def maximum(a, b, c, d, e):
    return max(a, b, c, d, e)


result = maximum(5, 15, 67, 0, 89)
print(result)


# Function to display a minimum value
def minimum(a, b, c, d, e):
    return min(a, b, c, d, e)


nums = minimum(20, 23, 14, 6, 29)
print(nums)


# Function to display numbers between 1 and 10
def print_numbers(nambari):
    for i in range(nambari):
        print(i)


print_numbers(10)
