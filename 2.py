while True:
    try:
        a=input()
    except:
        break
    if '//' in a:
        i=a.index('//')
        l=list(a)
        x=l[:i]
        y=l[i:]
        str1="".join(x)
        s=str1.replace('->','.')+"".join(y)
        print(s)
    else:
        print(a.replace('->','.'))