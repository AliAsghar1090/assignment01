#             3. Divisibility Check of two numbers
num1 = float(input("ENTER NUMERATOR:"))
num2 = float(input("ENTER DENOMERATOR:"))
ans = num1%num2
if ans == 0:
    print(num1," IS COMPELETLT DIVISABLE BY ",num2 )
else:
    print(num1," IS  NOT COMPELETLT DIVISABLE BY ",num2 )