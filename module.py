# Importing class modules to be executed
import my_module
import math
import statistics
import datetime

# Using predefined modules
my_module.hello("Erick")
my_module.hello("Daniel")
my_module.circle_area(7)

# Using math analysis in math
print(math.sqrt(16))
print(math.e)

# Analysing data contained in dataset using statistics module imported
dataset = [3, 5, 6, 7, 5, 8, 3]
x = statistics.mean(dataset)
y = statistics.mode(dataset)
z = statistics.median(dataset)
a = statistics.variance(dataset)
b = statistics.stdev(dataset)
c = statistics.quantiles(dataset)

print("The mean is " + str(x))
print("The mode is " + str(y))
print("The median is " + str(z))
print("The variance is " + str(a))
print("The standard deviation is " + str(b))
print("The Quantiles is " + str(c))

masaa = datetime.datetime.now()
print(masaa)
