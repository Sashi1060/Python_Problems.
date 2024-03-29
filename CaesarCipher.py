import random

def generate_random_key() -> int:
    return random.randint(1, 40)

def caesar_encrypt(plain_text: str, key: int) -> str:
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = key % 26  # Ensure shift is within the alphabet
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text: str, key: int) -> str:
    return caesar_encrypt(encrypted_text, -key)

key = generate_random_key()


plain_text = input("")
encrypted_text = caesar_encrypt(plain_text, key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")
