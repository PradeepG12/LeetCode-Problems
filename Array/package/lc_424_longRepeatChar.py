from collections import Counter


data = [
    ["ABAB",2 ],
    ["AABABBA",1],
    ["KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4]
]
def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    left, counter, mf, ml = 0, Counter(), 0, 0
    for right in range(n):
        counter[s[right]] += 1
        mf = max(mf, counter[s[right]])
        while (right-left+1)-mf > k:
           left+=1
           counter[s[left]] -= 1 
        ml = max(ml, right-left + 1)
    return ml


print([characterReplacement(d1, d2) for d1, d2 in data])