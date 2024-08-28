def calculate_pi(n_tems: int) -> float:
  numerator: float = 4.0
  denominator: float = 1.0
  operation: float = 1.0
  pi: float = 0.0
  for _ in range(n_tems):
    pi += operation * (numerator / denominator)
    denominator += 2.0
    operation *= -1.0
  return pi

if __name__ == "__main__":
  print(calculate_pi(1000000))