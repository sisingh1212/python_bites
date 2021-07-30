import string
import random
password_final=''

password_length=int(input("Whats the password length? "))

lower_letter=int(input("How many lower letters do you want?" ))
digit_letter=int(input("How many digits do you want?" ))

upper_letter=int(input("How many upperletters do you want?" ))

special_chars=int(input("How many special chars do you want?" ))

if len(password_final) < password_length:
    for ll in range(lower_letter):
        lower_letter_string=random.choice(string.ascii_lowercase)
        password_final=password_final+lower_letter_string

    
if len(password_final) < password_length:
    for ul in range(upper_letter):
        upper_letter_string=random.choice(string.ascii_uppercase)
        password_final=password_final+upper_letter_string

if len(password_final) < password_length:   
    for dig in range(digit_letter):
        digit_string=random.choice(string.digits)
        password_final=password_final+digit_string

if len(password_final) < password_length:   
    for i in range(special_chars):
        sp_string=random.choice(string.punctuation)
        password_final=password_final+sp_string
l=list(password_final)
random.shuffle(l)
print(''.join(l))
    
