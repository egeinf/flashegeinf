for A in range(100):
  flag = 1
  for x in range(1,1000):
    flag *= ((x % 3 == 0) <= (x % 5 != 0)) or (x+A >= 90)
  if flag:
    print(A)
    break

for A in range(100):
  flag = 1
  for x in range(1,1000):
    flag *= ((x % 2 == 0) <= (x % 5 != 0)) or (x+A >= 80)
  if flag:
    print(A)
    break

for A in range(100):
  flag = 1
  for x in range(1,1000):
    flag *= ((x % 3 == 0) <= (x % 5 != 0)) or (x+A >= 70)
  if flag:
    print(A)
    break