class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            rest = target - num

            for j, num1 in enumerate(nums):
                if i != j and num1 == rest:
                    return [i, j]
