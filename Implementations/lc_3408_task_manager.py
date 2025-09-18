from typing import List
import heapq
from collections import defaultdict


datas = {
    "tasks": [[1,101,10],[2,102,20],[3,103,15]],
    "add1": [4,104,5],
    "edit": [102,8],
    "top":[],
    "rmv": 101,
    "add2": [5,105,15]
}


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.updated_data = {}
        self.scheduler = self.__order_task(tasks)

    def __order_task(self, tasks):
        task_list = []
        for user_id, task_id, priority in tasks:
            self.updated_data[task_id] = (priority, user_id)
            heapq.heappush(task_list, (-priority, -task_id, user_id))
        return task_list

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.updated_data[taskId] = (priority, userId)
        heapq.heappush(self.scheduler, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        priority, userId = self.updated_data[taskId]
        self.updated_data[taskId] = (newPriority, userId)
        heapq.heappush(self.scheduler, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        self.updated_data.pop(taskId, None)

    def execTop(self) -> int:
        scheduler = self.scheduler
        while scheduler:
            priority, taskId, userId = heapq.heappop(scheduler)
            if -taskId in self.updated_data:
                current_priority, userId = self.updated_data[-taskId]
                if current_priority == -priority:
                    self.updated_data.pop(-taskId)
                    return userId

# ["TaskManager","add","edit","execTop","rmv","add","execTop"]
tm = TaskManager(datas["tasks"])
print(tm.scheduler, "\n", tm.updated_data, "\n")

a1, a2, a3 = datas["add1"]
tm.add(a1, a2, a3)
print(tm.scheduler, "\n", tm.updated_data, "\n")

e1, e2 = datas["edit"]
tm.edit(e1, e2)
print(tm.scheduler, "\n", tm.updated_data, "\n")

tm.execTop()
print(tm.scheduler, "\n", tm.updated_data, "\n")

r = datas["rmv"]
tm.rmv(r)
print(tm.scheduler, "\n", tm.updated_data, "\n")

a1, a2, a3 = datas["add2"]
tm.add(a1, a2, a3)
print(tm.scheduler, "\n", tm.updated_data, "\n")

tm.execTop()
print(tm.scheduler, "\n", tm.updated_data, "\n")