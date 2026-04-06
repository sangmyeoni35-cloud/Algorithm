from collections import deque

N, K = map(int, input().split())

# queue 숫자를 모두 enqueue
queue = deque()
for i in range(1,N+1):
    queue.append(i)

count = 1
print('<', end='')
while len(queue) > 1:
    person = queue.popleft()
    if count != K:
        queue.append(person)
        count += 1
    else:
        print(person, end=', ')
        count = 1
    
print(queue.popleft(), end='')
print('>')

