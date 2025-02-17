"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
"""
from typing import List

# python specific list
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums *2

# general solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        blank_list = [0] * (2*n)

        for i,v in enumerate(nums):
            blank_list[i] = v
            blank_list[i+n] = v

        return blank_list
    
if __name__ == '__main__':
    nums = [1,3,2,1]
    s = Solution()
    print(s.getConcatenation(nums))