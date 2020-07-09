f  = open('gymnastics.in', 'r')
lowCount = 0
highCount = 0
cowList = []
pairs = 0
line = f.readline()
K = int(line.split()[0])
N = int(line.split()[1])
count = 0
lowCount = 0
highCount = 0
entries = K*N
for i in range(K):
  line = f.readline()
  for j in range(N):
    x = int(line.split()[j])
    cowList.append(x)


for cow1 in range (1,N):
  for cow2 in range (cow1+1,N+1):
    # print('cows')
    # print(cow1)
    # print(cow2)
    # print('cows')
    count = 0
    lowCount = 0
    highCount = 0
    for i in range (K):
      for j in range (count*N,(count+1)*N):
        # print('j')
        # print (j)
        # print('j')
        if (cowList[j] == cow1):
          lowCount = lowCount + 1
          print('count')
          print(lowCount)
          print(highCount)
          print('count')
          count = count + 1
          if(lowCount == 3):
            print('pair')
            print(cow1)
            print(cow2)
            print('pair')
            pairs = pairs + 1
          # print(cow1)
          # print(cowList[j])
          print('break')
          break

        elif (cowList[j] == cow2):
          highCount = highCount + 1
          print('count')
          print(lowCount)
          print(highCount)
          print('count')
          count = count + 1
          # print('break')
          if(highCount == 3):
            pairs = pairs + 1
            print('pair')
            print(cow1)
            print(cow2)
            print('pair')
          # print(cow2)
          # print(cowList[j])
          break

print(pairs)
f = open('gymnastics.out', 'w')
f.write(str(pairs))
f.close()
