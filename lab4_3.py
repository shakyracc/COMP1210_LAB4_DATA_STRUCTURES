"""
# getting the factors of a number 6
list = []
for i in range (1, 7):
    
    if 6 % i == 0:
        list.append(i)
        print(list)

print(sum(list))
"""

# put in list comprehension form 

num = int(input("Enter a number: "))
print(sum([i for i in range(1, num + 1) if num % i == 0]))



