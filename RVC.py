# Global constants for character mappings
CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
CHAR_TO_NUM = {char: i for i, char in enumerate(CHARACTERS)}
NUM_TO_CHAR = {i: char for i, char in enumerate(CHARACTERS)}

def adjust_key_length(text: str, key: str) -> str:

    extended_key = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return extended_key

def encrypt(plain_text: str, key: str) -> str:
    
    key = adjust_key_length(plain_text, key)
    encrypted_text = ''
    
    for i, char in enumerate(plain_text):
        if char in CHAR_TO_NUM:
            total_shift = (CHAR_TO_NUM[char] + CHAR_TO_NUM[key[i]]) % len(CHAR_TO_NUM)
            encrypted_text += NUM_TO_CHAR[total_shift]
        else:
            encrypted_text += char  

    return encrypted_text

def decrypt(encrypted_text: str, key: str) -> str:
    
    key = adjust_key_length(encrypted_text, key)
    decrypted_text = ''

    for i, char in enumerate(encrypted_text):
        if char in CHAR_TO_NUM:
            total_shift = (CHAR_TO_NUM[char] - CHAR_TO_NUM[key[i]]) % len(CHAR_TO_NUM)
            decrypted_text += NUM_TO_CHAR[total_shift]
        else:
            decrypted_text += char  
            
    return decrypted_text

def valid_key(key: str) -> bool:
    """
    Checks if the key contains only valid characters.
    """
    return all(char in CHARACTERS for char in key)

# Main interaction
plain_text = input("Enter the plaintext: ")
key = input("Enter the key: ")

if valid_key(key):
        encrypted = encrypt(plain_text, key)
        print(f"Encrypted: {encrypted}")

        decrypted = decrypt(encrypted, key)
        print(f"Decrypted: {decrypted}")
else:
        print("Invalid key. Please use only characters in the defined set.")
    