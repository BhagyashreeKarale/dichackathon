# Write a Python program to print a dictionary in table format.
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# Sample Output:
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
dlist=[]
for key,values in my_dict.items():
    dlist.append(key)
    if type(values)==list:
        for i in values:
            dlist.append(i) 
    elif type(values)==dict:
        for j in values.values():
            dlist.append(j)
    else:
        dlist.extend([key,values])
print(dlist)
i=0
l=[]
fl=[]
count=0
for i in range(len(dlist)+1):
    if count!=0 and count%4==0:
        temp=l
        fl.append(temp)
        l=[]
    if i!=len(dlist):
        l.append(dlist[i])
    count=count+1
print(fl)

for e in range (len(fl)+1):
    for d in range (len(fl[e-1])-1):
        if e==e:
            print(fl[d][e],end=" ")
    print()
     




