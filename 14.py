# Q17.Write a Python program to sort a dictionary by key.

#ascending order
sample={"d":17,'a': 100,"z":26,'b':200,"y":28,'c':300}
keys=list(sample.keys())
fdic={}
for k in range(len(keys)):
    for i in range(len(keys)-k-1):
        if keys[i]>keys[i+1]:
            temp=keys[i]
            keys[i]=keys[i+1]
            keys[i+1]=temp
for a in keys:
    fdic[a]=sample[a]
print(fdic)

#descending order
sample={"d":17,'a': 100,"z":26,'b':200,"y":28,'c':300}
keys=list(sample.keys())
fdic={}
for k in range(len(keys)):
    for i in range(len(keys)-k-1):
        if keys[i]<keys[i+1]:
            temp=keys[i]
            keys[i]=keys[i+1]
            keys[i+1]=temp
for a in keys:
    fdic[a]=sample[a]
print(fdic)