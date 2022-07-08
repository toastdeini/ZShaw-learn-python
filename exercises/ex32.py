the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# Same as above...
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# We can also go through lists with mixed datatypes!
for i in change:
    print(f"I've got {i}")

# We can also build lists - start with an empty one
elements = []

# ...then use the range function to count
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # .append is a function that acts on lists
    elements.append(i)

# ...and now we can print that list!
for i in elements:
    print(f"Element was: {i}")