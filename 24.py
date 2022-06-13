# Текстовый файл состоит не более чем из 106 символов A, B и C.
# Найдите максимальное количество подряд идущих пар символов AB или AC.
# Искомая подстрока может включать только пары AB, только пары AC или содержать одновременно как пары AB, так и пары AC.
f = open('24.txt').readline()
max1 = 0
k = 0
for i in range(1, len(f), 2):
  if (f[i] == 'A' and f[i+1] == 'B') or (f[i] == 'A' and f[i+1] == 'C'):
    k += 1
    if k > max1:
      max1 = k
  else:
    k = 0
print(max1) # 7


f = open('24.txt').readline()
max2 = 0
k = 0
for i in range(0, len(f), 2):
  if (f[i] == 'C' and f[i+1] == 'B') or (f[i] == 'C' and f[i+1] == 'A'):
    k += 1
    if k > max2:
      max2 = k
  else:
    k = 0
print(max2) # 5