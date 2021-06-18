def nth_fib(n):
    num = []
    num.append(0)
    num.append(1)
    for i in range(2, n, 1):
        num.append(num[i-2] + num[i-1])
    return num[n-1]

    # https://www.codewars.com/kata/522551eee9abb932420004a0/train/python

    