#Project Euler
#Problem 10
#Summation of Primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

i = 2
j = 3

while j < 2000000:
    k = 3
    while k * k <= j and j % k != 0:
        k = k + 2
    if k * k > j:
        i = i + j
    j = j + 2

print(i)
