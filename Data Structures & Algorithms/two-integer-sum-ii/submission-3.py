class Solution:
    def twoSum(self, numbers: List[int], target: int):
        
        # it will be something like if the target is larger than the ints then save them
        # and then add them. 

        '''
        there is first index and the last one the possibility is 
        
        '''
        left = 0
        right = len(numbers)

        for i in numbers:
            if (numbers[left] + numbers[right-1]) > target:

                right = right - 1

            if (numbers[left] + numbers[right-1]) < target:
                left = left + 1

            if (numbers[left] + numbers[right-1]) == target:

                return [left+1, right]
