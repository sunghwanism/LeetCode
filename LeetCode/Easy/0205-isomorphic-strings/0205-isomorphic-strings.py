class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        str_dict = {}
        for i, _s in enumerate(s):
            if _s not in str_dict.values():
                str_dict[t[i]] = _s
                print(t[i], _s)
            else: # 있다면?
                print('_', _s)
                if t[i] not in str_dict.keys():
                    str_dict[t[i]] = '_'

        newWord = ''
        for _t in t:
            ch = str_dict[_t]
            newWord += ch

        return str(newWord) == s
        