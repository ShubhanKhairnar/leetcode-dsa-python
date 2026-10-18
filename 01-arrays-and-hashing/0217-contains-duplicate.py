class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = []

        for number in nums:
            if number not in seen:
                seen.append(number)
            else:
                return True

        return False