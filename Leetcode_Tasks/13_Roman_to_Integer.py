class Solution2:
    def romanToInt(self, s: str) -> int:
        roman_convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        length = len(s)
        roman_before = s[-1]
        result = 0
        for i in range(-1, -length - 1, -1):
            if roman_convert[roman_before] > roman_convert[s[i]]:
                result -= roman_convert[s[i]]
            else:
                result += roman_convert[s[i]]
            roman_before = s[i]
        return result

print(Solution2().romanToInt('MCMXCIV'))
