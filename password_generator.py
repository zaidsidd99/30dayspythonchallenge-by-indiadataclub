# Generate a random 8-character password ? 

import string
import random

def generate_password (length=8):
    characters= string.ascii_letters+ string.digits+ string.punctuation
    password= ''.join(random.choice(characters) for _ in range (length))
    return password
                       