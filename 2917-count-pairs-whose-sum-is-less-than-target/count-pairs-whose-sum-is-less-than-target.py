class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        count = 0
        nums.sort()

        while l <= r:
            if nums[l] + nums[r] < target:
                count += (r - l)
                l += 1
            else:
                r -= 1
        return count
            