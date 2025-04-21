x = "March 7, 2024"

"""
list = []

for character in x: 
    if character.isalpha():
        list.append(character)

print(list)
print(sorted(list))
"""

# use list comprehension 

print(sorted([character for character in x if character.isalpha()]))