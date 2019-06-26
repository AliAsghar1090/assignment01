#19. Palindrome tester
palin = input("Enter Text:")
rev = palin[::-1]

if palin == rev:
    print("Text", palin, "is Palindrome")
else:
    print("Text", palin, "is not a Palindrome")