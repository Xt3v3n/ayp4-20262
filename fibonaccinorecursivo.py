import time

"""def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

inicio = time.time()
print(f"El resultado es: {fibonacci(5)}")
print(f"Se demoro: {time.time() - inicio}")"""

def fibonacci_memo(n, cache={}):

    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
    return cache[n]

inicio = time.time()
print(f"El resultado es: {fibonacci_memo(5)}")
print(f"Se demoro: {time.time() - inicio}")
