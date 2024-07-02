#Comparison Operators
'''if the temperature is greater than 30
    its a hot down_payment
otherwise if its less then 10
    its a cold day
otherwise
    its neither hot or cold'''

temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

temperature = 30

if temperature != 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#Question-2
'''if name is less than 3 characters long 
    name must be at least 3 characters
otherwise if its more than 50 chracters long 
    name can be maximum of 50 characters 
otherwise
name looks good'''


name = input("Enter your name: ")

if len(name) < 3:
     print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be at most 50 characters")
else:
    print("Name looks good")

