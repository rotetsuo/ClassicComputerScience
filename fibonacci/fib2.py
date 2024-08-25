def fib2(n: int) -> int:
  if n < 2:  # caso base
    return n
  return fib2(n - 1) + fib2(n - 2)  # caso recursivo


# vai funcionar, mas com muitas chamadas, isto pode ser um probema como por exemplo seriam
# necessarias 21.891 chamadas para fib2(20)
