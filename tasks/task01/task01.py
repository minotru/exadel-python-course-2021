base = 10
for i in range(1, 1001):
    power = narcissistic_number = 0
    wp = wn = i
    while wp:
        power += 1
        wp //= base
    while wn:
        narcissistic_number += (wn % base) ** power
        wn //= base
    if narcissistic_number == i:
        print(narcissistic_number)
