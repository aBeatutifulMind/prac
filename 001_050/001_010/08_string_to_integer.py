class Solution:
    def myAtoi(self, str: str) -> int:
        if not str or len(str) == 0:
            return 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        sum = 0
        sign = 0
        for i in range(len(str)):
            if str[i] == ' ':
                continue

            # if none-white char is positive
            if str[i] == '+' or str[i].isdecimal():
                if str[i] == '+':
                    i += 1
                for j in range(i, len(str)):
                    if str[j].isdecimal():
                        sum = sum * 10 + int(str[j])
                        if sum >= INT_MAX:
                            return INT_MAX
                    else:
                        break
                return sum

            # if none-white char is negative
            if str[i] == '-':
                for j in range(i+1, len(str)):
                    if str[j].isdecimal():
                        sum = sum * 10 + int(str[j])
                        if -1 * sum <= INT_MIN:
                            return INT_MIN
                    else:
                        break
                return -1 * sum
            # if the first non-white char is invalid
            return 0
        # if the str only contains white space
        return 0






















