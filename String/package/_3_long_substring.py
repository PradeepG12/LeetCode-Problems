def lengthOfLongestSubstringBrute(s: str) -> int:
    n = len(s)
    maxi = 0
    for i in range(n):
        for j in range(i, n):
            if s[j] in s[i:j]:
                break
            maxi = max(len(s[i:j+1]), maxi)
    return maxi

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    seen = set()
    start = 0
    maxi = 0
    for end in range(n):
        while s[end] in seen:
            seen.remove(s[start])
            start+=1
        seen.add(s[end])
        maxi = max(maxi, end-start+1)
    return maxi
