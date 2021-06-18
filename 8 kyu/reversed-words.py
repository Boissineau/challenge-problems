def reverse_words(s):
    
    str = []
    tmp = ''
    prev = False
    for i in range(len(s)):
        tmp += s[i]
        if s[i] == ' ':
            
            str.append(tmp.strip())
            tmp = ''
            continue
    str.append(tmp)
    
    str = str[::-1]
    str2 = ''
    for i in str:
        str2 += i + ' '
    
    str2 = str2.strip()
    print(str2)
    return str2


def reverseWords(str):
    return " ".join(str.split(" ")[::-1])


    # https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python