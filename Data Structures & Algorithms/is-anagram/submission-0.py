class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check strings lengths, have to match, if not, return False
        #initiate 2 hashmaps, insert chars & their count in each hashmap
        #compare frequency count, should match --> return True
        #if not return False
        seen = set()
        if len(s)!=len(t):
            return False

        countS, countT = {}, {}

        for i in range (len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT




        