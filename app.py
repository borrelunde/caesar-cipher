from caesar_cipher import encrypt

plainText = 'Experience is the teacher of all things.'
offset = 3
cipher = encrypt(plainText, offset)

print('Caesar Cipher Demo:')
print(f'Plain text: {plainText}')
print(f'Offset: {offset}')
print(f'Cipher: {cipher}')
