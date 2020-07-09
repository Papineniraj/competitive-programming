f = open('outofplace.in', 'r')
line = f.readline()
selected = 0
switchIndex = 0
count = 0
N = int(line)
temp = 0
smallerCount = 0
list = []
oldList = []
changes = 0
# print(N)
for i in range (int(N)):
 line = int(f.readline())
 list.append(line)
 oldList.append(line)
# print(list)
for i in range (0,N):
  switchIndex = i
  # print(list)
  smallerCount = 0
  for j in range (i+1,N):
    if (list[j] < list[switchIndex]):
      while (((j+1) <= N-1) and (list[j+1] == list[j])):
        j = j+1
      switchIndex = j
      smallerCount = smallerCount + 1
  if (smallerCount >= 1):
    temp = list[i]
    count = count+1
    list[i] = list[switchIndex]
    list[switchIndex] = temp
    print(list)
# print('a')
# print(oldList)


print(count)
f.close()
f = open('outofplace.out', 'w')
f.write(str(count))
f.close()






