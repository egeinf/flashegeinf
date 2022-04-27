'''
2.1 not (x <= w) or (y == z) or y

X 1 X X
X 0 1 X
X X 0 1
'''

'''
2.2 not (x <= y) or (y == z) or y

X 0 X X
X 1 0 X
X X 1 0
'''

'''
2.3 not (x <= z) or (y == w) or not y

0 0 X X
0 X X X 
1 1 X 0
'''

for x in 0,1:
  for y in 0,1:
    for z in 0,1:
      for w in 0,1:
        F = not(x <= w) or (y == z) or y
        if F == 0:
          print(y,x,w,z)
print('')
for x in 0,1:
  for y in 0,1:
    for z in 0,1:
      for w in 0,1:
        F = not(x <= w) or (y == z) or y
        if F == 0:
          print(z,w,x,y)

print('')
for x in 0,1:
  for y in 0,1:
    for z in 0,1:
      for w in 0,1:
        F = not(x <= z) or (y == w) or not y
        if F == 0:
          print(x,z,y,w)