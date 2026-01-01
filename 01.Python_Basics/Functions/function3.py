def calcuteOperations(a, b):
    add = a + b
    mul = a * b
    div = a / b
    sub = a - b
    return add, mul, div, sub

a, b, c, d = calcuteOperations(10, 2)
print(f"Addition: ", a)
print(f"Multiplication: ", b)
print(f"Division: ", c)
print(f"Subtraction: ", d)