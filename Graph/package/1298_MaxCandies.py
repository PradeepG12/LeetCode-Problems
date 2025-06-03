
from collections import deque
from typing import List


def maxCandies(status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    
    candies_count = 0
    
    boxes = set(initialBoxes)
    have_keys = set()
    can_explore = deque(i for i in initialBoxes if status[i] == 1)
    
    visited = set()
    while can_explore:
        box = can_explore.popleft()
        if box in visited:
            continue
        visited.add(box)
        candies_count += candies[box]

        for key in keys[box]:
            if key not in have_keys:
                have_keys.add(key)
                if key in boxes and key not in visited:
                    can_explore.append(key)

        for new_box in containedBoxes[box]:
            if new_box not in boxes:
                boxes.add(new_box)
            if status[new_box] == 1 or new_box in have_keys:
                if new_box not in visited:
                    can_explore.append(new_box)

    return candies_count

print(maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]))
print(maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]))
