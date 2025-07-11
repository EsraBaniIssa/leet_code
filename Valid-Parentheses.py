class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parantheses_dict = {
            "(": ")",
            "[": "]",
            "{": "}",
              }
        for i in range(len(s)):
            if s[i] in parantheses_dict.keys():
                stack.append(parantheses_dict[s[i]])
            elif s[i] not in "}])" or len(stack)==0 or stack.pop()!=s[i]:
                return False
        return len(stack)==0