def fibo(n):
    a, b = 0, 1
    i, result = 0, []
    while i < n:
        result.append(a)
        a, b = b, a + b
        i += 1
    return result


fibo(6)
