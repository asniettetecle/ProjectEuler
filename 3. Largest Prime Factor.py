#Project Euler
#Problem 3
#Largest Prime Factor
#The prime factors of 13195 are 5, 7, 13 and 29
#What is the largest prime factor of the number 600851475143?

i = 600851475143

for j in range (2, i):
    if j * j > i:
        break
    while i % j == 0:
        i = i // j

print(i)

