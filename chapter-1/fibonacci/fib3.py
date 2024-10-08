from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}  #nossos caso base


def fib3(n: int) -> int:
  if n not in memo:
    memo[n] = fib3(n - 1) + fib3(n - 2)  # memoização
  return memo[n]


