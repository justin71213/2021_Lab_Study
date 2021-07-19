class Solution:
    def maxSumDivThree(self, nums: list) -> int:
        """
        source: https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space

        DP[0]: Maximum value that divisible by 3.
        DP[1]: Maximum value that divided by 3 with remainder 1.
        DP[2]: Maximum value that divided by 3 with remainder 2.
        """
        dp = [0, 0, 0]
        for num in nums:
            dp2 = dp.copy()  # <--- add this line
            for i in dp2:  # 3 cases
                dp[(num + i) % 3] = max(dp[(num + i) % 3], num + i)
        return dp[0]


if __name__ == "__main__":
    import time

    nums = [3, 6, 5, 1, 8]
    start = time.time()
    val = Solution().maxSumDivThree(nums)
    print("ans:", val)
    print("running time:", start - time.time())
