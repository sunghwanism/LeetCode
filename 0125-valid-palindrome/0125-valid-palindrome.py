# import re

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        filtered_str = list(filter(lambda s: s.isalnum(), s.lower()))
        # filtered_str = re.sub('\W', '', s).lower() # // Using Regex
        return filtered_str == filtered_str[::-1]

"""
[Use Regex]
- Use re.sub(pattern, replace, text)
- Change the 'pattern' to 'replace' in 'text'
- (!Caution!) It cannot replace "[-_]" pattern

\W : string+number
\D : number
\S : White space
[str] : 'a' --> pattern 'a' is target
"""