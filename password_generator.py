import random
import string

def password_generator(length= 12):
    lowercase_letter = string.ascii_lowercase
    uppercase_letter = string.ascii_uppercase
    digits = string.digits
    special_character = string.punctuation

    all_combine = lowercase_letter + uppercase_letter +digits + special_character

    password= ''.join(random.choice(all_combine) for _ in range(length))

    return password

password = password_generator(16)
print("Your Secured Password: ", password)