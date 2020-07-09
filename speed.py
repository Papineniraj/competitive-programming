from random import randrange
f = open('speeding.in', 'r')
line = f.readline().split()

limits = []
speeds = []
# limits[1] ... limits[40] = 75
# limits[41] ... limits[90] = 35
# limits [91] ... limits[100] = 45
n = int(line[0])
m = int(line[1])
max = 0
for i in range(n):
  line = f.readline().split()
  length = int(line[0])
  limit = int(line[1])
  for x in range(length):
    limits.append(limit)
for y in range(m):
  line = f.readline().split()
  length = int(line[0])
  speed = int(line[1])
  for z in range(length):
    speeds.append(speed)
for a in range(100):
  diff = speeds[a] - limits[a]
  if (diff > max):
    max = diff

print(max)

f.close()
f = open('speeding.out', 'w')
f.write(str(max) + '\n')
f.close()
