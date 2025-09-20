from collections import defaultdict, deque
from typing import List

# TODO: Need to optimize
class Router:

    def __init__(self, memoryLimit: int):
        self.max_size = memoryLimit
        self.packet_memory = deque()
        self.packet_size = 0
        self.destination_tracker = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        data = [source, destination, timestamp]
        if data in self.packet_memory:
            return False
        if self.packet_size >= self.max_size:
            old_source, old_destination, old_timestamp = self.packet_memory.popleft()
            if old_destination in self.destination_tracker:
                if [old_source, old_timestamp] in self.destination_tracker[old_destination]:
                    self.destination_tracker[old_destination].remove([old_source, old_timestamp])
            self.packet_size -= 1
        self.packet_memory.append(data)
        self.packet_size += 1
        self.destination_tracker[destination].append([source, timestamp])
        return True

    def forwardPacket(self) -> List[int]:
        if self.packet_memory:
            self.packet_size -= 1
            source, destination, timestamp = self.packet_memory.popleft()
            if destination in self.destination_tracker:
                if [source, timestamp] in self.destination_tracker[destination]:
                    self.destination_tracker[destination].remove([source, timestamp])
            self.packet_size -= 1
            return [source, destination, timestamp]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        count = 0
        if destination in self.destination_tracker:
            print(self.destination_tracker[destination])
            for source, timestamp in self.destination_tracker[destination]:
                if timestamp >= startTime and timestamp <= endTime:
                    count+=1
        return count

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
