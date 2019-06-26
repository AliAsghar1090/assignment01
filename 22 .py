# 22. Write a Python program to construct the following pattern
num = 5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")

    print()
for i in range(num,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()