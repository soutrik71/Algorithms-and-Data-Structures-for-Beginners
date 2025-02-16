"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

from typing import List


# creates a new list
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        clean_ls = [num for num in nums if num != val]
        return len(clean_ls)


# inplace theory 2 pointer approach
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            print(f"k:{k} , i:{i}")
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                print(f"nums:{nums}")

        print(f"final nums:{nums}")
        return k


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp
                k += 1

        print(f"final nums: {nums}")
        return k


if __name__ == "__main__":
    # print(Solution().removeElement([3, 2, 2, 3], 3))
    # print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
