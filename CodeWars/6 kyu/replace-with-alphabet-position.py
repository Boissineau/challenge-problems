def alphabet_position(text):
    text2 = text.lower()
    l = ''
    for idx, i in enumerate(text2):
        if i.isalpha():
            l += str(ord(i) - 96) + ' '

    l = l.strip()
    return l


# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python