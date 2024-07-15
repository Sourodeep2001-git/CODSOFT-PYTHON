import random
import string

def generate_password(length, use_upper, use_digits, use_special):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    all_characters = lower + upper + digits + special
    
    if len(all_characters) == 0:
        raise ValueError("No character sets selected. Please enable at least one character set.")
    
    password = []
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))
  
    remaining_length = length - len(password)
    if remaining_length > 0:
        password += random.choices(all_characters, k=remaining_length)
 
    random.shuffle(password)
    
    return ''.join(password)

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    return length, use_upper, use_digits, use_special

if __name__ == "__main__":
    try:
        length, use_upper, use_digits, use_special = get_user_input()
        password = generate_password(length, use_upper, use_digits, use_special)
        print("Generated Password: ", password)
    except ValueError as e:
        print("Error: ", e)
