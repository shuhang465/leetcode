# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
class Solution:
    def addDigits(self, num: int) -> int:
        def get_sum(num):
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit
            return total_sum
        total_sum = get_sum(num)
        while total_sum > 9:
            total_sum = get_sum(total_sum)
        return total_sum

