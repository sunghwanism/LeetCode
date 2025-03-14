class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""
            
        else:
            prefix = strs[0]

            for s in strs[1:]:
                print(s)
                while not s.startswith(prefix) and prefix:
                    prefix = prefix[:-1]
                    # print(prefix)

                if not prefix:
                    return ""

            return prefix
                