def factorial(n):
    fact = 1
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    for i in range(1, n + 1):
        fact *= i
    return fact
        

#testing
for i in range(1, 6):
    print(factorial(i))
