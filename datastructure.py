# This is a list

my_classmate = ["Erick", "John", "Purity", "Emily", 50]
print(my_classmate[2])
my_classmate[0] = "Ann"
print(my_classmate)
my_classmate.append("Michael")
my_classmate.insert(1, "Joan")
print(my_classmate)

car_names = ["Toyota", "Nissan", "Bugatti", "Subaru", "Ferrari", "Lamborghini"]
print(car_names)
print(car_names[3])
car_names.append("Mercedes")
print(car_names)

# This is a tuple
my_fav_fruits = ("Mangoes", "Pineapples", "Oranges", "Bananas", "Apples", "Strawberries", "Cherries", "Berries")
print("My favourite fruit is " + my_fav_fruits[2])

# fav_fruit = input("Enter a value between 0-7 for your favourite fruit? ")
# print("Your favourite fruits are " + my_fav_fruits[int(fav_fruit)])

# set datastructures
my_fav_cars = {"Toyota", "Mercedes", "Lamborghini", "Nissan", True, 45}
my_fav_cars.add("Rangerover")
print(my_fav_cars)

# dictionaries
cars = {
    "Name": "Range",
    "Make": "Rangerover",
    "Model": "suv",
    "Year": 2020,

}
print(cars)
print(cars["Name"])

operating_sys = {
    "Name": "Windows-11",
    "Make": "Microsoft",
    "For": "Pc",
    "Year": 2022,

}
print(operating_sys)
print(operating_sys["Name"])
