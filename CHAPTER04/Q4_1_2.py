def fib(n):
    C = []
    a, b = 0, 1
    while a < n:
        C.append(a)
        a, b = b, a + b
    return C


print(fib(1000))
