class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        stack = []

        for char in s:
            if char in hash_map:
                if not stack or stack.pop() != hash_map[char]:
                    return False
            else:
                stack.append(char)
        return not stack