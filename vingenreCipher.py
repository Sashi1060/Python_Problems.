
CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
CHAR_TO_NUM = {char: i for i, char in enumerate(CHARACTERS)}
NUM_TO_CHAR = {i: char for i, char in enumerate(CHARACTERS)}

def create_dicts():
    # Directly return global mappings
    return CHAR_TO_NUM, NUM_TO_CHAR

def encrypt(plain_text, key):
    key = adjust_key_length(plain_text, key)
    encrypted_text = ''

    for i, char in enumerate(plain_text):
        if char in CHAR_TO_NUM:
            total_shift = (CHAR_TO_NUM[char] + CHAR_TO_NUM[key[i]]) % len(CHAR_TO_NUM)
            encrypted_text += NUM_TO_CHAR[total_shift]
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(encrypted_text, key):
    key = adjust_key_length(encrypted_text, key)
    decrypted_text = ''

    for i, char in enumerate(encrypted_text):
        if char in CHAR_TO_NUM:
            total_shift = (CHAR_TO_NUM[char] - CHAR_TO_NUM[key[i]]) % len(CHAR_TO_NUM)
            decrypted_text += NUM_TO_CHAR[total_shift]
        else:
            decrypted_text += char

    return decrypted_text

def valid_key(key):
    return all(char in CHARACTERS for char in key)


def adjust_key_length(text, key):
    key_length = len([char for char in text if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'])
    extended_key = (key * (key_length // len(key) + 1))[:key_length]
    return extended_key

# Ensure the key is valid
# key = "Lemin@3456789123"
plainText = input("")
key = input("")

if valid_key(key):
    encrypted = encrypt(plainText, key)
    print(encrypted)

    decrypted = decrypt(encrypted, key)
    print(decrypted)
else:
    print("Invalid key.")
