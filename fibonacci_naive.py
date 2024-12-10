def naive_fib(n):
  if n <= 1:
    return n
  return naive_fib(n-1) + naive_fib(n-2)

n = 5

result = naive_fib(n)

print(f"The {n} th fibonacci number is {result}.")