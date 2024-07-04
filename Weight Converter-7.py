#Weight  convert program


weight = int(input("Enter your weight: "))

unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    convert_kg = weight * 0.45
    print(f'you are {convert_kg} kilos: ')
else:
    convert_lbs = weight / 0.45
    print(f'you are {convert_lbs} lbs: ')