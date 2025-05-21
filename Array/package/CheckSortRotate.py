def check(nums):
    count_breaks = 0
    n = len(nums)

    for i in range(n):
        # Compare current with next (using modulo for circular array)
        if nums[i] > nums[(i + 1) % n]:
            count_breaks += 1
        
        # If more than one break, it's not sorted and rotated
        if count_breaks > 1:
            return False

    return True

# Example Usage:
print(check([3, 4, 5, 1, 2]))  # True
print(check([2, 1, 3, 4]))     # False
print(check([1, 2, 3]))        # True
print(check([1, 1, 1]))        # True
print(check([1, 2, 3, 4, 5]))  # True