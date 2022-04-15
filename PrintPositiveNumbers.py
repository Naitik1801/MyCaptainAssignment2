lst = input('Enter numbers for the list:').split(',')
lst1= []
for i in range (0,len(lst)):
    if int(lst[i])>0:
        lst1.append(int(lst[i]))
print(lst1)
