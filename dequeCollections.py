from collections import deque

d = deque()
d.append(1)
d.appendleft(2)
d.appendleft(5)
d.pop()
d.popleft()

for i in d:
	print(i, end=" ")