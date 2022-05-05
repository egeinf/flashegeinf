# Найдите номер (тут через флаги)
a = 'АБРТЫ'
k = 0
flag = 0
for a1 in a:
  for a2 in a:
    for a3 in a:
      for a4 in a:
        for a5 in a:
          b = a1+a2+a3+a4+a5
          k += 1
          if 'ЫЫ' not in b and 'АА' not in b and flag == 0:
            res = k
            flag = 1
print(res)

a = 'ЕИНРСЬ'
k = 0
flag = 0
for a1 in a:
  for a2 in a:
    for a3 in a:
      for a4 in a:
        for a5 in a:
          b = a1+a2+a3+a4+a5
          k += 1
          if b.count('Ь') == 0 and 'ЕЕ' not in b and flag == 0:
            res = k
            flag = 1
print(res)

a = 'АПРСУ'
k = 0
flag = 0
for a1 in a:
  for a2 in a:
    for a3 in a:
      for a4 in a:
        for a5 in a:
          b = a1+a2+a3+a4+a5
          k += 1
          if a1 == 'У' and 'АА' not in b and flag == 0:
            res = k
            flag = 1
print(res)