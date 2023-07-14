def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

b = int(input("Enter a number: "))

c = factorial(b)

print(f"The factorial of {b} is {c}")
