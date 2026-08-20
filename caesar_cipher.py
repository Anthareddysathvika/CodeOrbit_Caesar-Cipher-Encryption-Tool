def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # Check if character is a letter
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


# Main Program
print("=== Caesar Cipher Encryption Tool ===")

text = input("Enter the text: ")
shift = int(input("Enter shift value (key): "))

encrypted = encrypt(text, shift)
decrypted = decrypt(encrypted, shift)

print("\nOriginal Text :", text)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)