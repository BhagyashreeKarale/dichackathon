# Q19.Write a Python program to remove duplicates from Dictionary.
student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},
                'id2': {'name': ['David'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},
                'id3': {'name': ['Sara'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},
                'id4': {'name': ['Surya'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},}

# Sample output:

output={'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 
'id4': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']}, 
'id1': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['Sara']}} 


student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},
                'id2': {'name': ['David'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},
                'id3': {'name': ['Sara'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},
                'id4': {'name': ['Surya'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},}
c=student_data.copy()
vlist=[]
flist=[]
for i in student_data.values():
    vlist.append(i)
    count=0
    for k in range(len(vlist)):
        if vlist[k]==i:
            count=count+1
            if count>=2:
                flist.append(i)
for keys in c.keys():
    if student_data[keys] in flist:
        del student_data[keys]
        break
print(student_data)



#another method:
student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},
                'id2': {'name': ['David'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},
                'id3': {'name': ['Sara'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},
                'id4': {'name': ['Surya'], 'class': ['V'], 
                        'subject_integration': ['english, math, science']},}
ndic={}
vlist=[]
for (key,value) in student_data.items():
    if type(value)==dict:
        if value not in vlist:
            vlist.append(value)
            ndic[key]=value
print(ndic)
