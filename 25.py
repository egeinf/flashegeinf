print('25.1:')
for x in range(123450000, 123459999):
  x = str(x)
  if x[6] == '6' and x[8] == '8':
    x = int(x)
    if x % 17 == 0:
      print(x, x // 17)

# 12345?6?8
# 012345678

print('25.2:')
for x in range(123450000, 123459999):
    x = str(x)
    if x[6] == '7' and x[8] == '8':
        x = int(x)
        if x % 29 == 0:
            print(x, x // 29)


# 12345X7X8
# 012345678
      
print('25.3:')
for x in range(123450000, 123459999):
    x = str(x)
    if x[-1] == '8' and x[6] == '7':
        x = int(x)
        if x % 23 == 0:
            print(x, x // 23)

# 1000000000
# 12345?7*8
# 012345678