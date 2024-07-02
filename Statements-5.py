#if it's a hot day,
# it's a hot day.
# Drink plenty of water,
# otherwise if it's cold,
# it's cold day
# Wear warm clothes
# otherwise
# it's a lovely weather.

is_hot = False
is_cold = True

if is_hot:
    print("It'S a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

#Question-1
'''Price of the house is $1M
if the buyer has gppd credit, they need to put down 10%
otherwise
they need to put down 20%
print the down payment '''

price = 1000000
good_credit = True

if good_credit:
    down_payment = price * 0.10
else:
    down_payment = price * 0.20
print(f"Down payment: ${down_payment}")

#Logical operations
'''if applicant has high income and good credit 
    Eligible for loan'''

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit: #Both the inputs needs to be true, its just like we are multiplying
    print("Eligible for loan with AND function")

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit: #Atleast one input has to be true,its jsut like we are adding.
    print("Eligible for loan with OR Function ")

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan with NOT function ")


#Comparison Operators
'''if the temperature is greater than 30 
    its a hot down_payment
otherwise if its less then 10
    its a cold day
otherwise
    its neither hot or cold'''

temperature = 3

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")














