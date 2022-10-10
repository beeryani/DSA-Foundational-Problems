class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hasht = {}
        array = []
        
        for idx in range(1, len(nums)+1):
            hasht[idx] = 1
        
        for idx in range(len(nums)):
            if nums[idx] in hasht:
                hasht[nums[idx]] += 1
            
        for idx in hasht:
            if hasht[idx] == 1:
                array.append(idx)
        
        return array
                
                
        