for i in range(1,1001):
    x = i
    n = 1
    while x >= 10 :
        x = x // 10
        n += 1
    x = i
    sum = 0
    while x > 0 :
        sum += (x % 10) ** n
        x = x // 10
    if i == sum:
        print(i)