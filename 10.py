# Q13.Write a Python program to sum all the items in a dictionary.
sample={'a': 100, 'b':200, 'c':300}
sum=0
for i in sample.values():
    sum=sum+i
print(sum,"is the sum of all the values in the dictionary")