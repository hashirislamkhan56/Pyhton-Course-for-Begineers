birth_year = input("Birth Year: ")
print(type(birth_year))
age = 2024 - int(birth_year) #converted the string to intiger using conversion function (INT)
print (type(age))
print(age)


#Ask a user their weight(in pounds),convert it to kilograms and print on the terminal
weight_lbs = input("Weight (lbs): ")
weight_kilogram = int(weight_lbs) * 0.45
print(weight_kilogram)
print(type(weight_kilogram))
