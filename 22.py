for x in range(100):
  res = x
  P = 10
  Q = 8
  K1 = K2 = 0
  while x <= 100:
    K1 = K1 + 1
    x = x + P
  while x >= Q:
    K2 = K2 + 1
    x = x - Q
  L = K1 + x
  M = K2 + x
  if L == 13 and M == 19:
    print(res) # 40
    break

for x in range(100):
  res = x
  P = 10
  Q = 8
  K1 = K2 = 0
  while x <= 100:
    K1 = K1 + 1
    x = x + P
  while x >= Q:
    K2 = K2 + 1
    x = x - Q
  L = K1 + x
  M = K2 + x
  if L == 10 and M == 19:
    print(res) # 70
    break