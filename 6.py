def rot13(message):
    cipher = ''
    for i in message:
        if i.isalpha():
            index = ((ord(i.lower()) - 96) + 13) % 26
            if index == 0:
                index = 26
            if i.isupper():
                cipher += str(chr(index + 96)).upper()
            else:
                cipher += str(chr(index + 96))
        else:
            cipher += i
    return cipher


# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python