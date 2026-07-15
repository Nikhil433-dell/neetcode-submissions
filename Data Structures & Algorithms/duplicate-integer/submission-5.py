class Solution:
    def hasDuplicate(self, nums: List[int]):
        
        nums.sort()

        if nums == []:
            return False

        else:
            first = nums[0]

            for i in range(1,len(nums)):
                if first == nums[i]:
                    return True
                first = nums[i]

            return False
