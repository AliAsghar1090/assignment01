# 15. Digits Sum of a Number
num = int(input("ENTER NUMBER:"))
total = 0
while (num > 0) :
    digit = num%10
    total = total+digit
    num = num//10
print(total)