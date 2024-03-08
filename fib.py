def fib(n):
    
    sum = 0
    if n <= 0:
        return None
    if n <= 2:
        return 1

    sum += fib(n - 1) + fib(n - 2)
    return sum  
    


for n in range(1, 10):  # testing
    print(n, "->", fib(n))