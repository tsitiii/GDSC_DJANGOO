def is_pal(s):
    result=s[::-1]
    if s==s[::-1]:
        
        return "is indeed a palindrome."
    else:
        return "not palindrome."
accept=input("Enter the word u wanna check: ")
word=is_pal(accept.lower())
print(f"Word {accept} is {word}")
