from collections import deque

stack = [] # Empty list

#Stack : FILO
#List append -> push,  pop -> out
stack.append(1)
stack.append(2)
stack.append(3)

stack.pop()

print(stack) # 최하단부터
print(stack[::-1]) # 최상단부터

#Queue: FIFO
#append, popleft
queue = deque() # for queue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

queue.popleft()

print(queue)

queue.reverse()

print(queue)