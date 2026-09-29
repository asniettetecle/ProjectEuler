#Project Euler
#Problem 9
#Special Pythagorean Triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a² + b² = c²
#For example, 3² + 4² = 9 + 16 = 25 = 5².
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

a = 1

while a < 1000:
    b = a + 1
    while b < 1000:
        c = 1000 - a - b
        if c > b and a * a + b * b == c * c:
            abc = a * b * c
            print(abc)
        b = b + 1
    a = a + 1
