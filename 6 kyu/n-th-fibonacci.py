def nth_fib(n):
    # this will work for very large numbers rather than the recursive solution
    num = []
    num.append(0)
    num.append(1)
    for i in range(2, n, 1):
        num.append(num[i-2] + num[i-1])
    return num[n-1]

    # https://www.codewars.com/kata/522551eee9abb932420004a0/train/python

    
def fib(n):
    if (n <= 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def fib2(n, memo = {}):
    if n in memo: 
        return memo[n]

    if (n <= 2):
        return 1

    memo[n] = fib2(n - 1, memo) + fib2(n - 2, memo)
    return memo[n]


print(nth_fib(50))
print(fib2(50))

