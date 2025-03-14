class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2:
            return False

        valid_dict = {"(":")", "[":"]", "{":"}"}

        front_list = []

        for _s in s:
            # print(_s, "||", front_list)

            if len(front_list) == 0:
                if _s in valid_dict.values():
                    return False
                else:
                    front_list.append(_s)

            else:
                if valid_dict[front_list[-1]]==_s:
                    front_list.pop()

                else:
                    if _s in valid_dict.values():
                        return False

                    else:
                        front_list.append(_s)

        if len(front_list) > 0:
            return False
        else:
            return True
