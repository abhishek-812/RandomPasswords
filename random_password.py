import random

def password_generator(hint):
    symbols = ["@","!","%","$","&","*","?"]
    
    if(len(hint)<8):
        password_length = 8
    else:
        password_length = len(hint)+4
        
    password = ""
    
    for i in range(password_length):
        nextIndex = random.randrange(len(hint))
        password = password + hint[nextIndex]
    
    # Replace 1 or 2 characters with a number
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(password)//2)
        password = password[0:replace_index] + str(random.randrange(10)) + password[replace_index+1:]
        
    # Replace 1 or 2 letters with an uppercase letter
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(password)//2,len(password))
        password = password[0:replace_index] + password[replace_index].upper() + password[replace_index+1:]
    
    # replace 1 or 2 letters with an symbols
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(password)//2)
        password = password[0:replace_index] + str(random.choice(symbols)) + password[replace_index+1:]
    
    return password

hint = input("Enter your hint to Create Password: ")
password = password_generator(hint)
print("Your password is " + (password))
print("if you want to fetch Created password with hint then type your hint else to exit type -1")
inp = input()
while inp != "-1":
    if(inp == hint):
        if(password.find(hint)):
            print(password)
    else:
        print("Please provide correct hint that you used at the time of creating Password")
    inp = input()
