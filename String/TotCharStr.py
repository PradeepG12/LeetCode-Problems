class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MODULO = 10**9 + 7
        z = "ab"
        for _ in range(t):
            transformed = []
            for char in s:
                if char == 'z':
                    transformed.append(z)
                else:
                    transformed.append(chr(ord(char)+1))
            s = ''.join(transformed)
            print(s)
        return len(s) % MODULO
        # MODULO = 10**9 + 7
        # z_count = s.count('z')
        # non_z_count = len(s) - z_count

        # final_length = non_z_count + (z_count * (2 ** t))
        # return final_length
    
soln = Solution()
res = soln.lengthAfterTransformations("abdcz",2)
print(res)