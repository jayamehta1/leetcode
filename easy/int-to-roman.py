'''
12. Integer to Roman

Medium

Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
'''


def intToRoman(self, num: int) -> str:
    m = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
         (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
         (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    result = ""
    for value, symbol in m:
        result += symbol*(num//value)
        num %= value
    return result


intput_num = 1994
print(intToRoman(0, intput_num))  # Output: "MCMXCIV"
