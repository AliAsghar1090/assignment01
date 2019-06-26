# 17. Binary to Decimal Converter
def bintodec(bin_num):
    power = 0
    dec_num = 0
    while bin_num > 0:
       dec_num += 2**power*(bin_num%10)
       bin_num //=10
       power +=1
    return dec_num
result = int(input("ENTER BINARY NUMBER:"))
print(str(bintodec(result)))