class Solution:
    def reverse(self, x: int) -> int:
        digits = [d for d in str(x) if d != "-"]

        digits.reverse()
        if int("".join(digits)) > 2147483647:
            return 0
        else:
            num = int("".join(digits))

        if (x > 0):
            return num
        else:
            return num * -1
