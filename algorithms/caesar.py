from constants.constants import letters

SHIFT = 11


def encrypt(text):
    translated = ''
    for symbol in text:
        if symbol in letters:
            num = letters.find(symbol)
            num = num + SHIFT
            if num > len(letters) - 1:
                num = num - len(letters)
            translated = translated + letters[num]
        else:
            translated = translated + symbol

    return translated


def decrypt(text):
    translated = ''
    for symbol in text:
        if symbol in letters:
            num = letters.find(symbol)
            num = num - SHIFT
            if num < 0:
                num = num + len(letters)
            translated = translated + letters[num]
        else:
            translated = translated + symbol

    return translated
