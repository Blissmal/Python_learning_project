# Defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")


# creating my object
person1 = Person("Erick", 30)
person1.say_hello()

person2 = Person("Dan", 20)
person2.say_hello()

person3 = Person("Bliss", 25)
person3.say_hello()


# create a class called cars with the following attributes/properties
# make, model, year then create a function that prints make, model and year
# Then create three objects


class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def properties(self):
        print(f"The car is from {self.make} company, the model is {self.model} and year of manufacture is {self.year}")


# creating the object
car1 = Cars("Toyota Motor Group", "Toyota", 1992)
car1.properties()

car2 = Cars("Honda Motor Group", "Honda", 1990)
car2.properties()

car3 = Cars("Mercedes Motor Group", "Mercedes", 2002)
car3.properties()


class Book:
    def __init__(self, title, author, year, terms):
        self.title = title
        self.author = author
        self.year = year
        self.terms = terms

    def display(self):
        print(
            f"The title of the book written by {self.author} is {self.title} with copyright {self.terms} "  
            f"was printed in the year {self.year}"
        )


book1 = Book("Computer Programming", "Albert Bliss", 1999, "2023 All Rights reserved")
book1.display()

book2 = Book("Blossoms", "Ole Henry", 2004, "2023 All Rights reserved")
book2.display()

book3 = Book("Treasures of the Earth", "Bliss", 2014, "2023 All Rights reserved")
book3.display()
