class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        res = []
        counter = 0

        while num > 0:
            rem = num%10
            if rem < 4:
                res.append(rem * roman_dict[1*(10**counter)])
            elif rem == 4:
                res.append(roman_dict[1*(10**counter)] + roman_dict[5*(10**counter)])
            elif rem < 9:
                res.append(roman_dict[5*(10**counter)] + (rem - 5) * roman_dict[1*(10**counter)])
            elif rem == 9:
                res.append(roman_dict[1*(10**counter)] + roman_dict[1*(10**(counter + 1))])
            counter +=1
            num = num//10
        return ''.join(res[::-1])

print(Solution().intToRoman(3749))