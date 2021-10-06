class Solution:
    def isHappy(self, n: int) -> bool:
        s = {n}
        while n != 1:
            tmp = sum([int(c) ** 2 for c in str(n)])
            if tmp in s:
                return False
            s.add(tmp)
            n = tmp
        return True