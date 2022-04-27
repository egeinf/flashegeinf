'''
5.1
На вход алгоритма. Строится двоичная запись числа N. Если N чётная - 10, если N нечетная слева - 1, справа - 01.
Укажите минимальное N для которого результат будет больше 88
'''

for N in range(100):
  res = N
  N = bin(N)[2:]
  if res % 2 == 0:
    N = str(N) + '10'
  else:
    N = '1' + str(N) + '01'
  N = int(N, 2)
  if N > 81:
    print('5.1:', res)
    break

for N in range(100):
  res = N
  N = bin(N)[2:]
  if res % 2 == 0:
    N = str(N) + '10'
  else:
    N = '1' + str(N) + '01'
  N = int(N, 2)
  if N > 441:
    print('5.2:', res)
    break


for N in range(100):
  res = N
  N = bin(N)[2:]
  if res % 2 == 0:
    N = str(N) + '10'
  else:
    N = '1' + str(N) + '01'
  N = int(N, 2)
  if N > 516:
    print('5.2:', res)
    break