def digital_root(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    if len(str(sum)) == 1:
        print(sum)
        return sum
    val = digital_root(sum)
    return val


# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python