#This line assigns value 100 of type int to variable named cars
cars = 100
#This line assigns value 4.0 of type float number to variable named space_in_car
space_in_car = 4.0
#this line assigns value 30 of type int to variable named drivers
drivers = 30
#this line assigns value 90 of type int to variable named passengers
passengers = 90
#this line assigns computed from variable cars - variable drivers to variable named cars_not_driven
cars_not_driven = cars - drivers
#this line assigns value of variable drivers to variable named cars_driven
cars_driven = drivers
#this line assigns value computed from multiplication of variable cars_driven and space_in_car and assigns it to variable named carpool_capacity
carpool_capacity = cars_driven * space_in_car
#this line computes passengers diveded bu cars_driven and assigns it to variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers , "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can trasport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to pu about", average_passengers_per_car, "in each car.")

