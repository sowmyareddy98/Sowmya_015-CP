def interleave(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    res = ""
    if l1 >= l2:
        for i in range(0,l2):
            res = res +s1[i]+s2[i]
        res = res +s1[l2:]
    else:
        for i in range(0,l1):
             res = res+s1[i]+s2[i]
        res=res+s2[l1:]
    return res    

print(interleave(input(), input()))