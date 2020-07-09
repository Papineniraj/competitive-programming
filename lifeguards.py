from random import randrange
f = open('lifeguards.in', 'r')
hours = [0 for i in range(1001)]
startingHour = 0
endingHour = 0
startingHours = []
endingHours = []
leastCovered = 1000
count = 0
hoursCovered = 0
line = f.readline()
n = line
print (n)
for i in range(int(n)):
  line = f.readline()
  startingHour = int(line.split()[0])
  endingHour = int(line.split()[1])
  startingHours.append(startingHour)
  endingHours.append(endingHour)
  for j in range (startingHour, endingHour):
    hours[j] = hours[j]+1
for i in range (0,1001):
  if (hours[i] > 0):
    hoursCovered = hoursCovered + 1
for i in range(int(n)):
  print('new')
  startingHour = startingHours[i]
  endingHour = endingHours[i]
  print(count)
  count = 0
  for j in range (startingHour, endingHour):
    if(hours[j] == 1):
      count = count + 1
  if (count < leastCovered):
    print('tiny'+ str(count))
    leastCovered = count
print(leastCovered)
print(hoursCovered-leastCovered)
f = open('lifeguards.out', 'w')
f.write(str(hoursCovered-leastCovered))
print(str(hoursCovered-leastCovered))
f.close()
print(hours)
