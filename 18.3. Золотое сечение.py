def golden_ratio(n):
  otv = []
  (x, y) = (0, 1)
  while x <= n:
      (x, y) = (y, x + y)
      if x <= n:
        otv.append(x)
  print((n + 1) / max(otv))
golden_ratio(int(input()))