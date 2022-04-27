x = 7 * 512 ** 1912 + 6 * 64 ** 1994 - 5 * 8 ** 1991 - 4 * 8 ** 1960 - 2022
res = ''
while x != 0:
  res += str(x % 8)
  x //= 8
print(res.count('7'))

x = 5 * 216 ** 3031 + 4 * 36 ** 3042 - 4 * 36 ** 3053 - 3064
res = ''
while x != 0:
  res += str(x % 6)
  x //= 6
print(res.count('5'))

x = 3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 2 ** 1050 - 2022
res = ''
while x != 0:
  res += str(x % 4)
  x //= 4
print(res.count('3'))