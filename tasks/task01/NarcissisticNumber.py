for k in range(1, 1001):
    n = 1
    numberToProcess = k
    listOfNumbers = list()

    while numberToProcess >= 10:
        listOfNumbers.append(numberToProcess % 10)
        numberToProcess = numberToProcess // 10
        n += 1
    if numberToProcess < 10:
        listOfNumbers.append(numberToProcess)

    sumOfDigits = 0
    for i in listOfNumbers:
        sumOfDigits += i ** n
    if sumOfDigits == k:
        print("{}, n={}".format(k, n))