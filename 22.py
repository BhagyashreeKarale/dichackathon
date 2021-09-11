# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
sample={"d":17,'a': 100,"z":26,'b':200,"y":28,'c':300}
vallist=list(sample.values())
for k in range (3):
    for i in range (len(vallist)-k-1):
        if vallist[i]>vallist[i+1]:
            temp=vallist[i]
            vallist[i]=vallist[i+1]
            vallist[i+1]=temp
    print(vallist[i+1])