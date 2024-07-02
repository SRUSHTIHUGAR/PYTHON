def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

num_terms = int(input("Enter the number of terms in Fibonacci series: "))
fib_series = fibonacci(num_terms)
print(f"Fibonacci series of {num_terms} terms:", fib_series)
