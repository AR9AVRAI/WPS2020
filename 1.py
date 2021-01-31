x=input()
y=input()
a=[]
b=[]
c=[]
if len(x)==len(y):
    l1=list(x)
    l2=list(y)
    for i in range(0,len(x)):
        o1=ord(l1[i])
        o2=ord(l2[i])
        b.append(o1)
        c.append(o2)
    if max(b)<max(c):
        for j in range(0,len(b)):
            z=b[j] - c[j]
            a.append(z)
        m=max(a)
        n=min(a)
        if m==a[0] or n==a[0]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")