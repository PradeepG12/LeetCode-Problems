from collections import deque

class SimpleQueue:

    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, data):
        self.queue.append(data)

    
    def dequeue(self):
        if not self.queue:
            return "Queue is Empty"
        return self.queue.popleft()

    def peek(self):
        if not self.queue:
            return "Queue is Empty"
        return self.queue[0]
        
    def reverse_queue(self):       
        stack = []
        while self.queue:
            stack.append(self.queue.popleft())

        while stack:
            self.queue.append(stack.pop())
        return list(self.queue)
    
    def display(self):
        return list(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)