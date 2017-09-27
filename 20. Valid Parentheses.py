class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ["{","[","("]:
                stack.append(c)
            if c in ["}","]",")"]:
                last = stack.pop()
                if c == "}" and last == "{":
                    continue
                elif c == "]" and last == "[":
                    continue
                elif c == ")" and last == "(":
                    continue
                else:
                    return False
        return True
                    
