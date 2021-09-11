# Q5. Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

#ascending order
Original={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
values=list(Original.values())
for i in range(len(values)):
    for k in range(len(values)-i-1):
        if values[k]>values[k+1]:
            temp=values[k]
            values[k]=values[k+1]
            values[k+1]=temp
ndic={}
for v in values:
    for key in Original.keys():
        if Original[key]==v:
            ndic[key]=v
print(ndic)


#descending order
Original={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
values=list(Original.values())
for i in range(len(values)):
    for k in range(len(values)-i-1):
        if values[k]<values[k+1]:
            temp=values[k]
            values[k]=values[k+1]
            values[k+1]=temp
ndic={}
for v in values:
    for key in Original.keys():
        if Original[key]==v:
            ndic[key]=v
print(ndic)