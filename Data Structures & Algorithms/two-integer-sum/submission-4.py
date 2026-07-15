class Solution:
    def twoSum(self, nums: List[int], target: int):
        result = set()

    
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]+nums[j] == target and i!=j: 
                    result.add(i)
                    result.add(j)

        return list(result) 