# WriteQ3. a Python script to generate and print a dictionary that contains a number (between 1 and n) 
# in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

num=int(input("enter a number"))
q3dic={}
for key in range(1,num+1):
    value=key*key
    q3dic[key]=value
print(q3dic)