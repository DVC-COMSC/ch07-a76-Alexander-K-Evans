
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num2) < len(num1):
    temp = num1
    num1 = num2
    num2 = temp

num3 = num1 + num2
print (num3) 
