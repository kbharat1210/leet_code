class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        return ' '.join(reversed(s.split()))