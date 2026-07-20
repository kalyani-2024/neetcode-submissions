class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        g1=set()
        g2=set()

        if (len(s)==len(t)):

            return sorted(s)==sorted(t)
        else:
            return False

        
            


        