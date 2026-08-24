class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        index = 0
        sign = 1
        if s[index] == "-":
            sign = -1
            index +=1
        elif s[index] == "+":
            index +=1

        num = 0
        while index < len(s) and s[index].isdigit():
            num = num*10 + int(s[index])
            index += 1

        num = sign * num
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX

        return num 