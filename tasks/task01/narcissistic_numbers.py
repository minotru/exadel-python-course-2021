for k in range(1, 1001):
    result=0
    count=0
    i = k
    j = k
    # count of digits in a number
    while j>0:
        count += 1
        j //= 10
    # result for every number
    while i:
        digit = i % 10
        result += digit ** count
        i //= 10
    # narcissism check
    if k == result:
        print (k)