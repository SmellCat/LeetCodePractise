class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums):
                if i == j:
                    break
                if v1 + v2 == target:
                    if i > j: i, j = j, i
                    return i, j


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    Solution().twoSum(nums, target)
