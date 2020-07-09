f  = open('whereami.in', 'r')
list = []
line = f.readline()
numChars = 0
sameCount = 0
matchCount = 0
breakout = 0
minChars = 0
N = int(line)
line = f.readline()
for char in line:
  list.append(char[0])

for i in range (1,N+1):
  print(minChars)
  if (breakout == 1):
        break
  for j in range (0,N-i):
    if (breakout == 1):
        break
    for k in range(0,N-i):
        if j == k:
            continue
        
      if (breakout == 1):
        break
      if (matchCount > 0):
        break
      sameCount = 0
      if ((j > k) or (j < k)):
        #   list[j:j+i] == list[k:k+i]
        for l in range(0,i):
          if (breakout == 1):
            break
          elif(list[j+l] != list[k+l]):
            if ((matchCount == 0) & (l == i) & (k == (N-i))):
              breakout = 1
              minChars = i
              break
            else:
              break
          else:
            sameCount = sameCount + 1
            if(sameCount == i):
              matchCount = 1
              break



f = open('whereami.out', 'w')
f.write(str(minChars))
f.close()
