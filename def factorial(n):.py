def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number."))
if number<0:
    print("\nEnter: Factorial not defined for negative number.")
else:
    result = factorial(number)
    print(f"\nThe factorial of {number} is {result}")