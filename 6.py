for s in range(1000):
  res = s
  s = (s-21) // 10
  n = 1
  while s > 0:
    n = n * 2
    s = s - n
  if n == 64:
    print(res)
    break

for s in range(1000):
  res = s
  s = (s-21) // 10
  n = 1
  while s > 0:
    n = n * 2
    s = s - n
  if n == 32:
    print(res)

for s in range(1000):
  res = s
  s = (s-10) // 7
  n = 1
  while s > 0:
    n = n * 2
    s = s - n
  if n == 8:
    print(res)
    break