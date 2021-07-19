class Solution:
    def twoSum(self, nums: int, target: int):
        """
        1. assume that each input would have exactly one solution
        2. you may not use the same element twice.
        """
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        goal = {}
        for idx, num in enumerate(nums):
            remaining = target - num
            if num in goal:
                return [goal[num], idx]
            else:
                goal[remaining] = idx


if __name__ == "__main__":
    import time

    nums = [1, 2, 3, 4, 6, 7]
    target = 9
    start = time.time()
    indexes = Solution().twoSum(nums, target)
    print(indexes)
    print("running time:", start - time.time())
