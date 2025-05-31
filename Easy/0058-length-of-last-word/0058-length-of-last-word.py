class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s_list = s.split(" ")

        last_idx = -1
        last_word = s_list[last_idx]
        print(s_list)

        while(last_word == ''):
            last_word = s_list[last_idx]
            last_idx -= 1
        
        return len(last_word)