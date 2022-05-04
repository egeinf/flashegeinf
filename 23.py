def make(x,y):
  if x == y:
    return 1
  if x > y:
    return 0
  if x < y:
    return make(x+2,y) + make(x*2,y)
n = make(1,20) * make(20,52)
print(n)

def make(x,y):
  if x == y:
    return 1
  if x > y:
    return 0
  if x < y:
    return make(x+2,y) + make(x*2,y)
n = make(1,16) * make(16,52)
print(n)

def make(x,y):
  if x == y:
    return 1
  if x > y:
    return 0
  if x < y:
    return make(x+2,y) + make(x*2,y)
n = make(1,18) * make(18,52)
print(n)