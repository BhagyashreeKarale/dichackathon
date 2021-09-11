# Q18.Write a Python program to get the maximum and minimum value in a dictionary.

#maximum
sample={"d":17,'a': 100,"z":26,'b':200,"y":28,'c':300}
numlist=list(sample.values())
for k in range(len(numlist)):
    for i in range(len(numlist)-k-1):
        if numlist[i]<numlist[i+1]:
            temp=numlist[i]
            numlist[i]=numlist[i+1]
            numlist[i+1]=temp 
print(numlist[i],"is maximum")

#minimum
sample={"d":17,'e':500,'a': 100,"z":26,'b':200,"y":28,'c':300}
numlist=list(sample.values())
for k in range(len(numlist)):
    for i in range(len(numlist)-k-1):
        if numlist[i]>numlist[i+1]:
            temp=numlist[i]
            numlist[i]=numlist[i+1]
            numlist[i+1]=temp 
print(numlist[i],"is minimum")