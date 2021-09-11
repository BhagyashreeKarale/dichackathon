# Q8.Write a Python program to check whether a given key already exists in a dictionary.


d={'A':1,'B':2,'C':3}
ui=input("Enter the key:\n")
keys=list(d.keys())
if ui in keys:
    print("Given key exists")
else:
    print("Given key doesn't exist")