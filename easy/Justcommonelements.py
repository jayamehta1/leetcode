'''python program to find out common elements betwwen two list'''

def commonelements(num1,num2):
    n1 = set(num1)
    n2 = set(num2)
    print(n1 & n2)
    return (n1 & n1)

a = [1,2,3,4,5,1,4]
b = [1,2,5,5,8]
commonelements(a,b)