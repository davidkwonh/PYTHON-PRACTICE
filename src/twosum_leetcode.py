nums = [2,7,11,15]
target = 9

class Solution(object):
    def twoSum(nums, target):
        for i in nums:
            print(i)
            for j in nums:
                print(j)
                if (i+j) == target:
                    return [nums.index(i),nums.index(j)]

print(Solution.twoSum(nums,target))





x = 1
i = 1
for i in range(128):
    x+=x
    i+=i
    print(x)

print(x)