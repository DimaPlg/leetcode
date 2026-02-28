class Palindrome:
    def longestPalindrome(self, s: str) -> str:
        index_of_palindrome = [0,0]
        length = len(s)
        for i in range(length):
            for j in range(length -1, i, -1):
                if s[i] == s[j] and j - i > index_of_palindrome[1] - index_of_palindrome[0]:
                    distance = int((j - i + 1)//2) + (0 if (j - i + 1)%2 else 1)
                    for bord in range(distance):
                        if s[bord + i] != s[j - bord]:
                            break
                        if j - 2*bord - i < 3 and j - i > index_of_palindrome[1] - index_of_palindrome[0]:
                            index_of_palindrome[0],index_of_palindrome[1] = i,j
        return s[index_of_palindrome[0]:index_of_palindrome[1] + 1]


# print(Palindrome().longestPalindrome("babad"))
# print(Palindrome().longestPalindrome("cbbd"))
# print(Palindrome().longestPalindrome("abbcccba"))
print(Palindrome().longestPalindrome("xaabacxcabaaxcabaax"))
