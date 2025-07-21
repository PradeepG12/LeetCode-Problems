def makeFancyString(s: str) -> str:
    new_s = ""
    count = 0
    for char in s:
        if not new_s:
            count = 1
        else:
            if char == new_s[-1]:
                if count >= 2:
                    continue
                count += 1
            else:
                count = 1
        new_s += char
    return new_s
# print(makeFancyString("aab"))
