def fib5(n: int) -> int:
  if n == 0: return n # caso especial
  last: int = 0 # inicialmente definido para fib5(0)
  next: int = 1 # inicialmente definido para fib5(1)
  for _ in range(1, n):
    last, next = next, last + next  
  return next