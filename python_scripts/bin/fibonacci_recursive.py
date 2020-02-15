#!/usr/bin/python


##With Memory optimization

fibonacci_cache = {}

def fibonacci(n):
    if type(n) != int:
        raise ValueError('Give integer nunber')
    if n < 0:
        raise ValueError('Give positive nunber')

    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    # elif n == 2:
    #     return 1
    elif n > 1:
        value = fibonacci(n-1)+fibonacci(n-2)
    fibonacci_cache[n] = value
    return value


##Without Memory optimization
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1)+fibonacci(n-2)


for i in range(101):
    print '{} : {}'.format(i, fibonacci(i))