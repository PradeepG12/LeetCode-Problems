def calculator(s, char1, char2, value):
    """Helper func to reduce chars and calculate the values."""

    stack = []
    total = 0
    for char in s:
        if stack and stack[-1] == char1 and char == char2:
            stack.pop()
            total += value
        else:
            stack.append(char)
    return "".join(stack), total

def maximumGain(s: str, x: int, y: int) -> int:
    """Function to return Maximum Gain"""

    char1, char2 = "a", "b"
    if x < y:
        x,y = y,x
        char1, char2 = char2, char1
    s, total1 = calculator(s, char1, char2, x)
    _, total2 = calculator(s, char2, char1, y)
    return total1+total2