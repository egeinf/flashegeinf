def F(n):
  if n < 3: return 2
  if n % 2 == 0:
    return F(n-2) + F(n-1) - n
  return F(n-1) - F(n-2) + 2 * n
print(F(32))

def F(n):
  if n < 3: return 2
  if n % 2 == 0:
    return F(n-2) + F(n-1) - 2 * n - 1
  return F(n-1) - F(n-2) + 2 * n - 2
print(F(20))

def F(n):
  if n < 3: return 2
  if n % 2 == 0:
    return F(n-1) + F(n-2) - n
  return F(n-2) - F(n-1) + 2 * n
print(F(30))