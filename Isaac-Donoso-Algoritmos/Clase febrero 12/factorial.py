def factorial(n,total=1):
    if n<=1:
        return total
    return factorial(n-1, n*total)

factorial(0)

def factorial_pro(n):
    if n<=1:
        return 1
    
    return n * factorial_pro(n-1)

print(factorial_pro(0))