class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.palindromeRecursion(s.lower(), 0, len(s) - 1)

    def palindromeRecursion(self, s, left, right):
        if left >= right: return True

        # must check if alphanumeric or not, if not, skip
        if not s[left].isalnum(): return self.palindromeRecursion(s, left + 1, right)
        if not s[right].isalnum(): return self.palindromeRecursion(s, left, right - 1)
        if s[left] != s[right]: return False
        return self.palindromeRecursion(s, left+1, right-1)
