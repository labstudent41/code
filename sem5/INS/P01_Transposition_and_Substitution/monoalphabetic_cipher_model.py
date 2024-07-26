def encrypt(s, p, ch):
    c = [''] * len(s)
    for i in range(len(s)):
        if s[i] in p:
            index = p.index(s[i])
            c[i] = ch[index]
        else:
            c[i] = s[i]
    return ''.join(c)

def decrypt(s, p, ch):
    p1 = [''] * len(s)
    for i in range(len(s)):
        if s[i] in ch:
            index = ch.index(s[i])
            p1[i] = p[index]
        else:
            p1[i] = s[i]
    return ''.join(p1)

if __name__ == "__main__":
    alphabets = []
    for i in range(97, 123):
        alphabets.append(chr(i))
    for i in range(65, 91):
        alphabets.append(chr(i))

    chars = [
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
        'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
        'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
        ]

    message = input("Enter message: ").lower()
    ciphertext = encrypt(message, alphabets, chars)
    print(ciphertext)
    plaintext = decrypt(ciphertext, alphabets, chars)
    print(plaintext)

