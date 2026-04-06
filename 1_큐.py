from collections import deque
queue = deque()

import sys
input = sys.stdin.readline

turn = int(input())
op_list = []

for _ in range(turn):
    op_list = input().split()
    op_0 = op_list[0]

    if op_0 == 'push':
        data = queue.append(op_list[1])
        # print(data)
    elif op_0 == 'pop':
        if queue:
            data = queue.popleft()
            print(data)
        else:
            print(-1)
    elif op_0 == 'size':
        print(len(queue))
    elif op_0 == 'empty':
        print(1 if not queue else 0)
    elif op_0 == 'front':
        print(queue[0] if queue else -1)
    elif op_0 == 'back':
        print(queue[-1] if queue else -1)
