class Solution:
    @staticmethod
    def make_hash(needle: str) -> int:
        res = 0
        mul = 31
        for item in needle:
            res *= 31
            res += (ord(item) - ord('a')) * 31
            # print(res)
        return res

    def strStr(self, haystack: str, needle: str) -> int:
        if not len(needle):
            return 0
        if len(haystack) < len(needle):
            return -1
        needle_hash = self.make_hash(needle)
        target_hash = 0
        temp = 1
        for i in range(len(needle)):
            target_hash *= 31
            target_hash += (ord(haystack[i]) - ord('a')) * 31
            temp *= 31
        if target_hash == needle_hash:
            return 0
        for i in range(len(needle), len(haystack)):
            target_hash -= (ord(haystack[i - len(needle)]) - ord('a')) * temp
            target_hash *= 31
            target_hash += (ord(haystack[i]) - ord('a')) * 31
            if target_hash == needle_hash:
                return i - len(needle) + 1
        return -1
