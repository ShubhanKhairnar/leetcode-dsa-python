class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0

        for number in nums:
            digits = len(str(number))

            if digits % 2 == 0:
                count += 1

        return count
