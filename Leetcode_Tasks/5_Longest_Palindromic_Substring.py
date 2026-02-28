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

    def longestPalindromev2(self, s: str) -> str:
        length = len(s)
        res = [0,0]

        for i in range(length):
            st = end = i
            while st > -1 and end < length and s[st] == s[end]:
                st -= 1
                end += 1
            temp = [st + 1,end]
            if temp[1] - temp[0] > res[1] - res[0]:
                res = temp

            st, end = i, i + 1
            while st >= 0 and end < length and s[st] == s[end]:
                st -= 1
                end += 1
            temp = [st + 1,end]
            if temp[1] - temp[0] > res[1] - res[0]:
                res = temp

        return s[res[0]:res[1]+1]

# print(Palindrome().longestPalindrome("babad"))
# print(Palindrome().longestPalindrome("cbbd"))
# print(Palindrome().longestPalindrome("abbcccba"))
print(Palindrome().longestPalindromev2("xaabacxcabaaxcabaax"))
