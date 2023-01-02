class Solution:
    def detectCapitalUse(self, w: str) -> bool:
        return w in [w.upper(), w.lower(), w.capitalize()]