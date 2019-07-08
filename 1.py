#! /usr/bin/env python3 
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#
div5 = []
div3 = []
for i in range(0, 1000, 5):
    div5.append(i)
#print(div5)

for i in range(0, 1000, 3):
    div3.append(i)

div35 = set(div3 + div5)


total = sum(div35)
print(total)
