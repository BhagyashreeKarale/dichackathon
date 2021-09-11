# Q21.Write a Python program to print all unique values in a dictionary. 
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
SampleData = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
              {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
vallist=[]
uniqdic={}
for i in SampleData:
    for val in i.values():
        if val not in vallist:
            vallist.append(val)
print(vallist)#list
uniqdic["unique values"]=vallist
print(uniqdic)#dictionary