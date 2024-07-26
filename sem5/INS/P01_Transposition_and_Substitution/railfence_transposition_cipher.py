from math import ceil

def rail_fence_encrypt(text, key):
    rail = [['' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):

        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    ciphertext = ''
    for i in range(len(rail)):
        for j in range(len(rail[i])):
            if rail[i][j] == '':
                continue
            ciphertext += rail[i][j]
    return ciphertext

def rail_fence_decrypt(ciphertext, key):
    rail = [['' for i in range(len(ciphertext))] for j in range(key)]
    dir_down = False
    length = len(ciphertext)
    cycle = 2 * (key - 1)
    k = ceil(length / cycle)
    row, col = 0, 0

    i = 0
    for row in range(key):
        for col in range(row, length, cycle):
            rail[row][col] = ciphertext[i]
            i += 1

    text = ''
    row = 0
    for col in range(length):
        text += rail[row][col]
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        if dir_down:
            row += 1
        else:
            row -= 1
    return text


text = "HAPPY BIRTHDAY"
key = 2

ciphertext = rail_fence_encrypt(text, key)
print("\nEncrypted text: ", ciphertext)
plaintext = rail_fence_decrypt(ciphertext, key)
print("\nDecrypted text: ", plaintext)

