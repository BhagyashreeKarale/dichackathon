# Q27.Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

# Sample input if key is id: then 6
dic={}
for i in range(len(student)):
    for keys in student[i].keys():
        dic[keys]=student[i][keys]
   
print(dic)

