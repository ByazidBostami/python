dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count=0
mylist=[]
for i in dict_1.values():
    for j in i:
        mylist.append(j)
    
for i in mylist:
    count=count+1
print(count)
