'''202. Happy Number
Easy

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
'''

def isHappy(n) :
        num = set()
 

        while n != 1 and n not in num:
            num.add(n)
            sum = 0 

            while n > 0:
                digit = n % 10
                sum += digit * digit
                n = n // 10
            n = sum 
        print(n==1)    

        return n == 1 


n = 19
isHappy(n)