cnvrt_from = input("Enter the unit convert from 'Kg, gram lbs, Ltr, ml ")
cnvrt_to = input("Enter the unit convert to 'Kg, gram, lbs, ml, Ltr ")
amount = float (input('Provide the number as per the unit you want to convert: '))

if cnvrt_from == "kg" and cnvrt_to == 'gram':
    result = amount * 1000
    print(f'{amount} kg is equal to  {result} grams')
elif cnvrt_from == "gram" and cnvrt_to == 'kg':
    result = amount / 1000
    print(f'{amount} grams is equal to  {result} kg')
elif cnvrt_from == "gram" and cnvrt_to == 'lbs':
    result = amount / 453.592
    print(f'{amount} grams is equal to  {result} lbs')
elif cnvrt_from == "lbs" and cnvrt_to == 'gram':
    result = amount * 453.592
    print(f'{amount} lbs is equal to  {result} grams')
elif cnvrt_from == "lbs" and cnvrt_to == 'kg':
    result = amount / 2.20462
    print(f'{amount} lbs is equal to  {result} kg')
elif cnvrt_from == "ml" and cnvrt_to == 'Ltr':
    result = amount / 1000
    print(f'{amount} ml is equal to  {result} Ltr')
elif cnvrt_from == "Ltr" and cnvrt_to == 'ml':
    result = amount * 1000
    print(f'{amount} Ltr is equal to  {result} ml')
elif cnvrt_from == "Ltr" and cnvrt_to == 'ml':
    result = amount / 1000
    print(f'{amount} Ltr is equal to  {result} kg')
else: print("Invalid input")
