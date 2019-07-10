#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#----------
# Python Program to find the factors of a number

# define a function
# This function takes a number and prints the factors

# to take number input from user
x = int(input("Enter a number: "))
total = [ ]
primetotal = [ ]
for i in range(1, x + 1):
    if x % i == 0:
        total.append(i)
print (total)
for y in total:
    for m in range(2, y):
        if y % m == 0:
            break
    else:
        primetotal.append(y)
print(primetotal)
#print(total)
