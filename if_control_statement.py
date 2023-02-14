# if statement
x = 1
marks = 50
grade = 90

if x > 0:
    print("The number is positive")
# if ...else statement

if marks >= 50:
    print("You have passed the exam")
else:
    print("You have failed the exam")

# if....elif...else statement
if grade <= 30 and grade >= 0:
    print("You failed")
elif grade >= 30 and grade <= 49:
    print("You have passed")
elif grade >= 50 and grade <= 79:
    print("You have a credit")
elif grade >= 80 and grade <= 100:
    print("You have a distinction")
else:
    print("Wrong grade entered")

charges = 2000

if charges >= 0 and charges <= 499:
    print("You can borrow a loan")
elif charges >= 500 and charges <= 999:
    print("Pay 500 cash today to borrow more loan")
elif charges >= 1000 and charges <= 1999:
    print("You cannot borrow a loan unless you pay")
elif charges >= 2000:
    print("You have high charges crime rate")
else:
    print("Check the validity of your charges")
