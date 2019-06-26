#.20 Count Alphabets, Numbers and Special Characters
string = input("Enter text:")

list_alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list_Alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list_num = ["0","1","2","3","4","5","6","7","8","9"]
list_spc = " "

count_alpha = 0
count_num = 0
count_spc = 0
count_special = 0

for alpha in string:
     if alpha in list_alpha :
         count_alpha += 1
     elif alpha in list_Alpha:
         count_alpha += 1
     elif alpha in list_num:
         count_num += 1
     elif alpha in list_spc:
         count_spc +=1
     else:
         count_special += 1
print("Alphabates:",count_alpha)
print("Numbers:",count_num)
print("Spaces:",count_spc)
print("Special character:",count_special)