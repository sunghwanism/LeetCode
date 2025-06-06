class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1: "I", 5:"V", 10:"X", 50:"L",
                      100:"C", 500:"D", 1000:"M"}

        num = str(num)
        length = len(num)
        num_list = []

        result = ""

        for n in num:
            num_list.append(int(n)*10**(length-1))
            length -= 1

        for n in num_list:
            order = int(10**(len(str(n))-1))
            count = int(n/order)

            if count in (1,2,3):
                result += roman_dict[order]*count

            elif count == 4:
                result += str(roman_dict[order])+str(roman_dict[(count+1)*order])
            
            elif count == 5:
                result += roman_dict[count*order]
            
            elif count in (6, 7, 8):
                result += roman_dict[5*order]

                for _ in range(count - 5):
                    result += roman_dict[order]

            elif count == 9:
                result += str(roman_dict[order]) + str(roman_dict[(count+1)*order])


        return result