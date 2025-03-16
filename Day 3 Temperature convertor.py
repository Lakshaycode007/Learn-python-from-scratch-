# Fahrenheit to celsius convertor
unit = input("Enter the unit of temperature (F/C/K): ")
temp = float(input("Enter the temperature: "))

if unit == "F":
    result = (temp -32) * 5/9
    print(f"{temp}°F is equal to {result}°C")
elif unit == "C":
    result  =  ((temp * 9) / 5 + 32)
    print(f"{temp}°C is equal to {result}°F")
elif unit == "K":
    result =  temp - 273.15
    print(f"{temp}°K is equal to {result}°C")
else: print("Invalid unit")
