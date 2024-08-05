alphabets = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]

chars = [
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
    'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
    'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
    ]

def encrypt(text):
    ciphertext = ''
    for char in text:
        if char in alphabets:
            ciphertext += chars[alphabets.index(char)]
        else:
            ciphertext += char
    return ciphertext

def decrypt(text):
    plaintext = ''
    for char in text:
        if char in chars:
            plaintext += alphabets[chars.index(char)]
        else:
            plaintext += chars
    return plaintext

if __name__ == "__main__":
    message = input("Enter message: ").lower()
    ciphertext = encrypt(message)
    print("Encrypted Text:", ciphertext)
    plaintext = decrypt(ciphertext)
    print("Decrypted Text:", plaintext)

