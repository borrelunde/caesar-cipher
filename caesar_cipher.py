def encrypt(text, shift):
    result = ""
    for char in text:
        if char_is_invalid(char):
            result += char
            continue
        if char.isupper():
            result += encrypt_upper_char(char, shift)
        else:
            result += encrypt_lower_char(char, shift)
    return result


def encrypt_upper_char(char, shift):
    return chr((ord(char) + shift - 65) % 26 + 65)


def encrypt_lower_char(char, shift):
    return chr((ord(char) + shift - 97) % 26 + 97)


def char_is_invalid(char):
    num = ord(char)
    return not ((48 <= num <= 57) or
                (65 <= num <= 90) or
                (97 <= num <= 122))
