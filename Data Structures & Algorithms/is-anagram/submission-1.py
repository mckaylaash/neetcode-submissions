class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = list(s)
        str1.sort()
        str1 = " ".join(str1)

        str2 = list(t)
        str2.sort()
        str2 = " ".join(str2)

        if (str1 == str2):
            return True
        return False
            

        