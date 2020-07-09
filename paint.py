f = open('teleport.in', 'r')
line = f.readline()
a = int(line.split()[0])
b = int(line.split()[1])
x = int(line.split()[2])
y = int(line.split()[3])
distance = 0
if ((a - x) % 100) < ((x - a) % 100):
  axDistance = ((a - x) % 100)
else:
  axDistance = ((x - a) % 100)
if ((a - y) % 100) < ((y - a) % 100):
  ayDistance = ((a - y) % 100)
else:
  ayDistance = ((y - a) % 100)
if ((b - x) % 100) < ((x - b) % 100):
  bxDistance = ((b - x) % 100)
else:
  bxDistance = ((x - b) % 100)
if ((b - y) % 100) < ((y - b) % 100):
  byDistance = ((b - y) % 100)
else:
  byDistance = ((y - b) % 100)

if (axDistance <= ayDistance):
  distance = (axDistance + byDistance)
else:
  distance = (bxDistance + ayDistance)

print (distance)

f = open('teleport.out', 'w')
f.write(str(distance))
f.close()
