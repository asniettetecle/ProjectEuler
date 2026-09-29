#Project Euler
#Problem 5
#Smallest Multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 2520
j = 1

while j <= 20:
    if i % j == 0:
        j = j + 1
    else:
        i = i + 2520
        j = 1

print(i)
