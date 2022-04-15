def most_frequent(ch):
    s = set(ch)
    l = list(s)
    d = {}
    for i in range(len(l)):
        count = 0 
        for j in range(len(ch)):
            if l[i] == ch[j]:
                count +=1
        d.update({l[i]:count})
    print(sorted(d.items(),key=lambda x:x[1],reverse =True))
most_frequent('Mississippi')
