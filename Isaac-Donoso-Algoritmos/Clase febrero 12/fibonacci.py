def fibonacci(n):
    n0=0
    n1=1
    print(n0)
    print(n1)
    for i in range(n-1):
        total=n1+n0
        print(total)
        n0=n1
        n1=total
    

"""def fibonacci_recursividad(n):
    if n <= 1:
        return n
    return fibonacci_recursividad(n-1) + fibonacci_recursividad(n-2)"""


n = int(input("Ingrese la cantidad de numeros de fibonacci que deseas sacar: "))
fibonacci(n)


  