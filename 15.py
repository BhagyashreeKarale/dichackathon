# Q17.Write a Python program to sort a dictionary by value.



#ascending order
sample={"d":17,'a': 100,"z":26,'b':200,"y":28,'c':300}
vallist=[]
v=list(sample.values())
fdic={}
for j in range(len(v)):
    for i in range(len(v)-1-j):
        if v[i]>v[i+1]:
            temp=v[i]
            v[i]=v[i+1]
            v[i+1]=temp
for values in v:
    for keys in sample.keys():
        if sample[keys]==values:
            fdic[keys]=values
print(fdic)



#descending order
sample={"d":17,'a': 100,"z":26,'b':200,"y":28,'c':300}
vallist=[]
v=list(sample.values())
fdic={}
for j in range(len(v)):
    for i in range(len(v)-1-j):
        if v[i]<v[i+1]:
            temp=v[i]
            v[i]=v[i+1]
            v[i+1]=temp
for values in v:
    for keys in sample.keys():
        if sample[keys]==values:
            fdic[keys]=values
print(fdic)