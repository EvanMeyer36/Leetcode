class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = 0
        answer = int(dividend / divisor)
        if dividend == -2147483648 and divisor == -1: return 2147483647
        return answer