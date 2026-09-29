#Project Euler
#Problem 4
#Largest Palindrome Product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
#Find the largest palindrome made from the product of two 3-digit numbers.

i = 0

for j in range(100, 1000):
    for k in range(j, 1000):
        product = j * k

        digits = []
        n = product
        while n > 0:
            digits.append(n % 10)
            n = n // 10

        if digits == list(reversed(digits)):
            if product > i:
                i = product

print(i)
