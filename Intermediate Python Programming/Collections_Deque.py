from collections import deque

d = deque()

d.append(1)
d.append(3)

d.appendleft(2)

print(d)

d.pop()

print(d)

d.popleft()

print(d)

d.clear()

print(d)


d.append(5)
d.append(6)
d.append(7)
d.append(8)
d.append(10)
d.append("9hunna")

print(d)
print(d[5])
print(d[0])
d[4] = 9
print(d)

d.extendleft([4, 3, 2,])
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)
