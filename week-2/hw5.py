# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.

def twoSum(nums, target):
    # your code here
    size = 0
    for i in nums:
        size += 1

    for j in range(size):
        for k in range(size-1, j, -1):
            if (nums[j] + nums[k]) == target:
                # print("[",nums[j],",",nums[k],"]")
                return [j, k]
        

result = twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9