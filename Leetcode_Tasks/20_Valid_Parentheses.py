# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class ValidParentheses:
    def isValid(self, s: str) -> bool:
        left_brackets =[]
        brackets ={'(':')','[':']','{':'}'}
        left_brack = ['(', '{', '[']
        for i in range(len(s)):
            if s[i] in left_brack:
                left_brackets.append(s[i])
            else:
                if not left_brackets:
                    return False
                left_bracket = left_brackets.pop()
                if brackets[left_bracket] != s[i]:
                    return False
        return len(left_brackets)==0




print(ValidParentheses().isValid("()[]{}"))
print(ValidParentheses().isValid("([])"))
print(ValidParentheses().isValid("){"))
print(ValidParentheses().isValid("({{{{}}}))"))
print(ValidParentheses().isValid("){[}}{"))
print(ValidParentheses().isValid("[{}()]"))
print(ValidParentheses().isValid('(){}}{'))
print(ValidParentheses().isValid("[({])}"))