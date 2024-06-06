def caesar_encode(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

# Example usage
plaintext = "Hello, World!"
shift = 3
ciphertext = caesar_encode(plaintext, shift)
print("Ciphertext:", ciphertext)