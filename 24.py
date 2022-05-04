f = open('24.txt').readline()
max1 = 0
k = 0
for i in range(0, len(f), 2):
  if (f[i-1] == 'A' and f[i] == 'B') or (f[i-1] == 'A' and f[i] == 'C'):
    k += 1
    if k > max1:
      max1 = k
  else:
    k = 0
print(max1) # 7


f = open('24.txt').readline()
max2 = 0
k = 0
for i in range(1, len(f), 2):
  if (f[i-1] == 'C' and f[i] == 'B') or (f[i-1] == 'C' and f[i] == 'A'):
    k += 1
    if k > max2:
      max2 = k
  else:
    k = 0
print(max2) # 5