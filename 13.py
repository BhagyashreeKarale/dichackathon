# Q16.Write a Python program to map two lists into a dictionary.
l1=[1,2,3,4,5,6,7]
l2=["riya","ankita","rahul","priya","anshika","rose","aarti"]
dic={}
for i in range(len(l1)):
    dic[(l1[i])]=l2[i]
print(dic)


#using zip function
dic=dict(zip(l1,l2))
print(dic)