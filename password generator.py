import random
import string

number_of_list=int(input("enter the number: ")) 
letter_of_list=int(input("enter the number of letters:"))
if (number_of_list<0 or letter_of_list<0):
    print("the number must be in positive")
    exit()

password_letters=''.join(random.choice(string.ascii_letters) for i in range (number_of_list))
password_numbers=''.join(random.choice(string.digits) for i in range (letter_of_list))

password=password_letters+password_numbers
if (len(password)>6):
    print("Password must be in 6 digits")
    exit()
    
if (len(password)<6):
    print("password should contain 6 digits. enter the total number within 6")
    exit()
    
print('your passwword is {} '.format(password))