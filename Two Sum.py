# -*- coding: utf-8 -*-

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

__author__ = 'Atituiset'


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
