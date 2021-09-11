# Q1.Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})



d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key1 in d1.keys() and d2.keys():
    if key1 in d2.keys() and key1 in d1.keys():
        d1[key1]+=d2[key1]
    elif key1 not in d1.keys() and key1 in d2.keys():
        d1[key1]=(d2[key1])
print(d1)



