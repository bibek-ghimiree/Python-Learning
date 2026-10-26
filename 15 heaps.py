import heapq

numbers = [7, 2, 9, 1, 5]

heapq.heapify(numbers)
print(numbers)

heapq.heappush(numbers, 3)
smallest = heapq.heappop(numbers)

print("Smallest:", smallest)
print("Remaining heap:", numbers)


numbers = [10, 4, 7, 1, 9, 2]

print(heapq.nsmallest(3, numbers))
print(heapq.nlargest(3, numbers))

tasks = []
heapq.heappush(tasks, (2, "Write notes"))
heapq.heappush(tasks, (1, "Study Python"))
heapq.heappush(tasks, (3, "Practice coding"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, task)