# Q14.Write a Python program to multiply all the items in a dictionary.
sample={'a': 100, 'b':200, 'c':300}
result=1
for i in sample.values():
    result=result*i
print(result,"is the product of all the values in the dictionary")