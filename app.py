from caesar_cipher import encrypt

plain_text = 'Experience is the teacher of all things.'
offset = 3
cipher = encrypt(plain_text, offset)

print('Caesar Cipher Demo:')
print(f'Plain text: {plain_text}')
print(f'Offset: {offset}')
print(f'Cipher: {cipher}')
