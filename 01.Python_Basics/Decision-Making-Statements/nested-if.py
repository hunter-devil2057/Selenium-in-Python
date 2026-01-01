# Nested If statements
a = 100
if a%2==0:
    if a>5:
        print(a, 'is an even number and is also greater than 5')
    else:
        print(a, 'is an even number and is not greater than 5')
else:
    print(a, 'is an odd number')

if a>5:
    print("Yes", a, " is greater than 5")

if a>15:
    print("Yes", a, " is greater than 15")


if a<15:
    print("Yes", a, " is less than 15")


if a % 2==0:
    print(a, " is Even")
else:
    print(a, " is Odd")