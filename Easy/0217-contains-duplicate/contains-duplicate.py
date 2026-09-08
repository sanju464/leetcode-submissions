class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:  # Single loop: runs at most n times
            if num in seen:  # O(1) instantaneous lookup
                return True
            seen.add(num)
            
        return False