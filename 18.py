#18. Vowel and Consonants Counter
sent = input("ENTER SENTENCE: ")
string = sent.lower()
count1 = 0
count2 = 0
vowels = ["a","e","i","o","u"]
for ans in string:
    if ans in vowels :
        count1 +=1
    else :
        count2 +=1
print("vowels ",count1)
print("constants ",count2)