# 2. Create a Python project to get the value of e to n number of decimal places.

from math import e

number_of_decimal_places = int(input("Enter the number of decimal places you want to see: "))
limit = 0
length_of_e = []
value_of_e = str(e)

for x in value_of_e:
    limit = limit + 1
    # print(limit)
    length_of_e.append(x)

    if limit == number_of_decimal_places + 2:
        break

limit = ''.join(length_of_e)
print(limit)