from package import CircularQueue

c_queue = CircularQueue(5)
c_queue.enqueue(4)
c_queue.enqueue(5)
c_queue.enqueue(6)
c_queue.enqueue(7) 
c_queue.enqueue(9)
print(c_queue.display())
c_queue.dequeue()
c_queue.enqueue(9)
print(c_queue.display())
print(c_queue.peek())