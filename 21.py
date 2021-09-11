# Write a Python program to create and display all combinations of letters, 
# selecting each letter from a different key in a dictionary. Go to the editor
# # Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

Sampledata = {'1':['a','b'], '2':['c','d']}
a,b = Sampledata.values()
# print(a,b)
for i in a:
    for j in b:
        print(i,j)


for x in Sampledata['1']:
    for y in Sampledata['2']:
        print(x + y)
