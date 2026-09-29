#Project Euler
#Problem 7
#10001st Prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

i = 2
k = 1

while k < 10001:
    i = i + 1
    j = 2
    while j * j <= i:
        if i % j == 0:
            i = i + 1
            j = 2
        else:
            j = j + 1
    k = k + 1

print(i)
