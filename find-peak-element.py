# coding=utf-8

"""
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def findPeakElement(nums):
    """
    时间复杂度O(N)
    :param nums: 
    :return: 
    """
    for i, v in enumerate(nums):
        if (nums[i] > nums[i + 1]):
            return i
    return len(nums) - 1


def findPeakElement2(nums):
    """
    时间复杂度logN
    :param nums: 
    :return: 
    """
    return search(nums, 0, int(len(nums) - 1))


def search(nums, l: int, r: int):
    if l == r:
        return l
    mid = int((l + r) / 2)
    if nums[mid] > nums[mid + 1]:
        return search(nums, l, mid)
    return search(nums, mid + 1, r)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(findPeakElement(nums))
    print(findPeakElement2(nums))
