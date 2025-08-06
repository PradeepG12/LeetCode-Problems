from collections import defaultdict
data = ["abcabc", "aaacb", "abc"]

def numberOfSubstrings(s: str) -> int:
    n = len(s)
    left = 0
    count = 0
    hash_table = {"a":0, "b":0, "c":0}
    for right in range(n):
        hash_table[s[right]] += 1
        while hash_table["a"] > 0 and hash_table["b"] > 0 and hash_table["c"] > 0:
            count += n - right
            hash_table[s[left]] -= 1
            left += 1
    return count
print([numberOfSubstrings(d) for d in data])
