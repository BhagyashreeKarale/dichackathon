# Q20.Write a Python program to check a dictionary is empty or not.
dic={}
sample={'a': 100, 'b':200, 'c':300}

#using length:
def dicindicator1(dictionary):
    if len(dictionary)==0:
        print("Dictionary is empty")
    else:
        print("Dictionary isn't empty")

#using bool:
def dicindicator2(dictionary):
    if bool(dictionary)==False:
        print("Dictionary is empty")
    else:
        print("Dictionary isn't empty")

