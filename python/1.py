import sys
digit_string = sys.argv[1]

suma = 0
for i in digit_string:
    suma += int(i)

print(suma)
