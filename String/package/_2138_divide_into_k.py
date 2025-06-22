from typing import List


def divideString(s: str, k: int, fill: str) -> List[str]:
    # output = []
    # temp = ''
    # for char in s:
    #     temp += char
    #     if len(temp) == k:
    #         output.append(temp)
    #         temp = ''
    # print(output)
    # if temp:
    #     temp += fill * (k-len(temp))
    #     output.append(temp)
    # print(output)
    reminder = len(s) % k
    if reminder != 0:
        s += fill * (k-reminder)
    return [s[i:i+k] for i in range(0, len(s), k)]
