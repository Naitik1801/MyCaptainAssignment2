n = int(input('No of terms:'))
n1,n2 = 0,1
count = 0
while count < n:
    print(n1)
    n3 = n2+n1
    n1 = n2
    n2 = n3
    count += 1
