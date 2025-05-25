from collections import deque

class CircularQueue:
    def __init__(self, capacity):
        
        self.queue = [0] * capacity
        self.size = capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if self.full():
            raise "Max size reached"
        
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
    
    def dequeue(self):
        if self.isEmpty():
            raise "Queue is empty"        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return self.queue[self.front]
    
    def display(self):
        
        output = []        
        if self.front == -1:
            return output
        i = self.front
        while True:
            output.append(self.queue[i])
            if i == self.rear:
                break
            i = (i+1) % self.size
        return output

    def full(self):
        return (self.rear+1) % self.size == self.front
    
    def isEmpty(self):
        return self.front and self.rear == -1
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[self.front]