# Q4. Identify the Character Type...

char=input("Enter the character: ")

if char.isalpha():
    if char.lower() in 'aeiou':
        print("vovwel")
    else:
        print("consant")
    
elif char.isdigit():
    print("Digit")

else:
    print("Special character")
   
