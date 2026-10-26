from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print(queue)

first = queue.popleft()
print(first)  # A

print(queue)  # B, C


queue = deque([10, 20, 30])

print(queue[0])     # Front item
print(len(queue))   # Queue size

queue.append(40)    # Enqueue
queue.popleft()     # Dequeue

print(queue)