####### Решение Excel: drive.google.com/drive/folders/1Hg_qDNTp30HBleRp4l0wzJ95IdjdAqdv
f = open('17.txt')
a = [int(i.strip()) for i in f]

# Мин. элемент последовательности кратный 23
ost23 = []
for i in range(len(a)):
  if a[i] % 23 == 0:
    ost23.append(a[i])
delitel = min(ost23)
# Пары которые делятся на Мин. элемент последовательности кратный 23
k = 0
pair = []
for i in range(len(a)):
  if (a[i-1] % delitel == 0) or (a[i] % delitel == 0):
    k += 1
    pair.append(a[i-1] + a[i]) # Сумма элементов одной пары
print(k, max(pair))
##################################################################### 17.2
f = open('17.txt')
a = [int(i.strip()) for i in f]

# Мин. элемент последовательности кратный 23
ost4 = []
for i in range(len(a)):
  if a[i] % 4 == 0:
    ost4.append(a[i])
delitel = min(ost4)
# Пары которые делятся на Мин. элемент последовательности кратный 23
k = 0
pair = []
for i in range(len(a)):
  if (a[i-1] % delitel == 0) or (a[i] % delitel == 0):
    k += 1
    pair.append(a[i-1] + a[i]) # Сумма элементов одной пары
print(k, max(pair))

##################################################################### 17.3
f = open('17.txt')
a = [int(i.strip()) for i in f]

# Мин. элемент последовательности кратный 23
ost17 = []
for i in range(len(a)):
  if a[i] % 17 == 0:
    ost17.append(a[i])
delitel = min(ost17)
# Пары которые делятся на Мин. элемент последовательности кратный 23
k = 0
pair = []
for i in range(len(a)):
  if (a[i-1] % delitel == 0) or (a[i] % delitel == 0):
    k += 1
    pair.append(a[i-1] + a[i]) # Сумма элементов одной пары
print(k, max(pair))