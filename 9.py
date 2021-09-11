# Q9.Write a Python program to iterate over dictionaries using for loops.

# Example 1: Access both key and value using items()
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)
# a juice
# b grill
# c corn
# Using a for loop, pass two loop variables key and value for iterable dt.items(). 
# items() returns the key:value pairs.
# Print key and value.

# Example 2: Access both key and value without using items()
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt:
    print(key, dt[key])
# Output
# a juice
# b grill
# c corn
# Iterate through the dictionary using a for loop.
# Print the loop variable key and value at key (i.e. dt[key]).
# However, the more pythonic way is example 1.


# Example 3: Return keys or values explicitly
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt.keys():
    print(key)

for value in dt.values():
    print(value)
# Output
# a
# b
# c
# juice
# grill
# corn
