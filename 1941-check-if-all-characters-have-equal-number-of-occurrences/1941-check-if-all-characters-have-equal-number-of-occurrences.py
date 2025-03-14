class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)

        if len(set(cnt.values())) == 1:
            return True
        else:
            return False
