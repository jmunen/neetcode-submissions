class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #loop through - for loop
        #create an empty set - seen
        #if number not in seen, add it
        #return True
        #at the end of the loop return False
        
        seen = set ()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False

        